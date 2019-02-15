#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import pandas as pd
import string
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
import vaderSentiment
import re

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
#
# print extract_textfeatures_flavor2("are you fucking stupid? shut up ugly bitch!!!")

# def divide_tasks(k,tau,task):
#     #input k: number of initial give comments
#     #input tau: time lag
#     #note: data X_i is the same across all tasks, need to generate target set Y
#     X = pd.read_csv("")
# def create_tasks(tau,k,)
tau = 15
k = 10
threshold = 5
import os
directory = 'tau='+str(tau)+'_k='+str(k)
if not os.path.exists('tau='+str(tau)+'_k='+str(k)):
    os.makedirs(directory)
print directory
data = pd.read_csv('raw_text_labeled.csv').iloc[:,1:]
D = pd.DataFrame()
for t in range(int((148-k)/tau))[:10]:
    # print t
    X = []
    Y = []
    for i in range(204):
        print t,i
        X_i = []
        session_i = data[data['idx'] == i]
        # print session_i
        len_session_i = len( data[data['idx'] == i])
        max_t = int((len_session_i-k)/tau)

        # for t in range(1,max_t+1):

        for j in range(len_session_i-t*tau-k):
            window = session_i.iloc[j:j+k]['comment']#.values.flatten().tolist()


            window = ' '.join([x.split('(created at')[0] for x in window])

            X.append(list(extract_textfeatures_flavor2(window))+[i])
            x_task_t = window
            list_y = [1 if x == 'T' else 0 for x in session_i.iloc[j:j + k + t * tau]['label'].tolist()]
            Y.append(list_y)
    if len(X)>0:
        df = pd.concat((pd.DataFrame(X),pd.DataFrame(Y).sum(axis =1)),axis =1)
        df.columns = ['textlen','punc','uppercase','badwords','vader','hashtag','user','url',
                  'fuck', 'bitch', 'shut', 'hate', 'suck', 'gay', 'ugli', 'work', 'beauti', 'sick','idx','label']
        df.to_csv(directory+'/task_'+str(t)+str('.csv'),index = False)
        if not os.path.exists(directory + '/train'):
            os.makedirs(directory + '/train')
        if not os.path.exists(directory + '/test'):
            os.makedirs(directory + '/test')
        x_train, x_test, y_train, y_test, = train_test_split(
            df.iloc[:,:-2], df['label'], test_size=0.3, random_state=42)

        x_train['label'] = y_train
        x_test['label'] = y_test
        # print x_train,x_test
        x_train.to_csv(directory + '/train/task_' + str(t) + '.csv', index=False)
        x_test.to_csv(directory + '/test/task_' + str(t) + '.csv', index=False)