#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import pandas as pd
import collections
import numpy as np
import string
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler,SMOTE
import vaderSentiment
import re
import datetime
from dateutil.relativedelta import relativedelta
import csv
def extract_textfeatures_flavor2(comment):
    words = ['fuck', 'bitch', 'shut', 'hate', 'suck', 'gay', 'ugli', 'work', 'beauti', 'sick']
    analyzer = vaderSentiment.SentimentIntensityAnalyzer()
    vader = analyzer.polarity_scores(comment).get('compound')
    f = pd.read_csv('Terms-to-Block.csv')['0'].tolist()
    ps = PorterStemmer()
    wordnet_lemmatizer = WordNetLemmatizer()
    words = [ps.stem(wordnet_lemmatizer.lemmatize(w)) for w in words]
    comment = unicode(comment, errors='ignore')
    comment = comment.decode('utf-8').encode('ascii', errors='ignore')
    punc = sum([comment.count(i) for i in ["!", "?"]])
    url =len(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', comment))
    user = len(re.findall(r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9-_]+)', comment))
    hashtag = len(re.findall(r"#(\w+)", comment))
    comment = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",comment).split())
    textlen = len(comment.split())
    if textlen ==0:
        textlen =1
    punc = punc/textlen
    uppercase = len(filter(lambda x: x in string.uppercase, comment)) / textlen
    comment = [x.lower() for x in comment.split()]
    comment = [ps.stem(wordnet_lemmatizer.lemmatize(w)) for w in comment]
    comment = " ".join(comment)
    badwords = sum([comment.count(i) for i in f])/textlen
    # for uni in [comment.count(x) for x in words]:
    #     return uni
    unigrams = [comment.count(x) for x in words]
    all_features = tuple([textlen,punc,uppercase,badwords,vader,hashtag,user,url]+unigrams)

    # return textlen,punc,uppercase,badwords,vader,hashtag,user,url,tuple(unigrams)
    return all_features


def extract_temporalfeatures_flavor2(comments,idx):
    #input list of comments and the index of session they belong to
    data = pd.read_csv('sessions_40plus_metadata.csv')['cptn_time'].tolist()[idx]
    t0_str = '2'+data.strip('Media posted at ')
    t0 = datetime.datetime.strptime(t0_str,'%Y-%m-%d %H:%M:%S') 
    ct= []
    for comment in comments:
        end = datetime.datetime.strptime(comment.split('created at:')[-1].strip(')'),'%Y-%m-%d %H:%M:%S')
        diff = relativedelta(end,t0)
        diff_hour = diff.years*8760+diff.months*730+diff.days*24+diff.hours+diff.minutes*0.017
        ct.append(diff_hour)
    if len(ct)>2:
        delta_t=[round(x - ct[i - 1],3) for i, x in enumerate(ct)]
    else:
        delta_t = ct
    time2first = ct[0]
    ICI_mean = np.mean(delta_t)+0.0001
    ICI_var = np.std(delta_t)**2
    ICI_coef = np.std(delta_t)/ICI_mean
    x = ct
    t_N = max(x)
    line = range(int(t_N))
    at= 0
    for t in line:
       if sum([ t - xx for xx in x if xx < t ])!=0:
            at+= sum([ np.exp(-2*(t - xx)) for xx in x if xx < t ])
    at_mean = np.mean(at)
    return time2first,ICI_mean,ICI_var,ICI_coef,at,at_mean

# print extract_temporalfeatures_flavor2(['Cool nail but I dont bite on mine (created at:2012-08-07 03:46:09)', '@offthis_ way to be a asshole (created at:2012-11-24 03:57:26)'],0)

D = pd.DataFrame()
Y = []
I= []
labeled_data = pd.read_csv('raw_text_labeled.csv')
idx = labeled_data['idx'].tolist()

# for i in list(set(idx))[:]:
#     session_i = labeled_data[labeled_data['idx']==i]
#     l = labeled_data[labeled_data['idx']==i]['label'].tolist()
#     for j in range(len(session_i)):
#         first_j_comments = session_i['comment'].iloc[:j+1].values.flatten().tolist()
#         # Temporal = extract_temporalfeatures_flavor2(first_j_comments,int(i))
#         first_j_comments = ' '.join([x.split('(created at')[0] for x in first_j_comments])
#         Textual = extract_textfeatures_flavor2(first_j_comments)
#         print i,j,[l[:j+1].count('T')/5 if l[:j+1].count('T')<=5 else 1][0]
#         file = open('features/flavor2/textual+unigrams/train/task' + str(j) + '.csv','a+')
#         csv.writer(file, lineterminator='\n').writerow((i,[l[:j+1].count('T')/5 if l[:j+1].count('T')<=5 else 1][0])+Textual)
#         file.close()

#
#
unlabeled_data = pd.read_csv('raw_text_unlabeled.csv')
idx = unlabeled_data['idx'].tolist()
for i in list(set(idx)):
    session_i = unlabeled_data[unlabeled_data['idx']==i]
    for j in range(len(session_i))[:]:
            first_j_comments = session_i['comment'].iloc[:j+1].values.flatten().tolist()
            # Temporal = extract_temporalfeatures_flavor2(first_j_comments,int(i))
            first_j_comments = ' '.join([x.split('(created at')[0] for x in first_j_comments])
            Textual = extract_textfeatures_flavor2(first_j_comments)
            print i,j
            file = open('features/flavor2/textual+unigrams/test/task' + str(j) + '_alltasks.csv','a+')
            csv.writer(file, lineterminator='\n').writerow((i,)+Textual)
            file.close()
