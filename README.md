# CyberBullying Prediction On Instagram
Fixed-Lag Varing-Horizon (FLVH) and Fixed-Horizon Varing-Lag (FHVL) models are provided in this project. 

### Prerequisites
#### Matlab
```
MALSAR [1]
```
#### Python 2
```
NLTK
vaderSentiment
SKlearn
Pandas
```

### How to use
In each model folder, there are the following files available:
``` raw_text_labeled.csv: a sample labeled dataset
    create_tasks.py: create tasks for multi-task learning
    train_test.py: create training and testing data
    mtl.mat: find the optimize W using MALSAR and save W matrix as a csv file
    load.py: load W from the csv file
    mtl_regression.py: for prediciton  
```

### Dataset
We use a corpus of 10 thousand comments, manually annotated as harassing or not by 10 experts. We focus on harassing comments due to their commonality to a number of types of unwanted behavior, including cyberharassment and cyberbullying. We used this data to evaluate our method for [robust and timely detection of cyberbullying](https://dl.acm.org/citation.cfm?id=3313462) as well as for [harashment anticipation](https://doi.org/10.1145/3292522.3326024).

Our labeled corpus spans 22.1% of all media sessions containing at least 40% profanities in the dataset introduced by [2]. Of all media sessions containing at least 40% profanities, 47.5% had been labeled as positive if:
> there are negative words and/or comments with intent to harm someone or other, and the posts include two or more repeated negativity against a victim [2].

#### Dataset Access
Email us at cchelmis@albany.edu if you are interested in our dataset! We are happy to share our data with you.

#### Citation
If you use this code and/or dataset, please cite
> Mengfan Yao, Charalampos Chelmis, and Daphney Zois. Cyberbullying Ends Here: Towards Robust Detection of Cyberbullying in Social Media. The 2019 World Wide Web Conference (WWW ’19), May 2019.

> Charalampos Chelmis and Mengfan Yao. Minority Report: Cyberbullying Prediction on Instagram. In 11th ACM Conference on Web Science (WebSci ’19), July 2019

BibTeX
``` 
@inproceedings{yao2019cyberbullying,
  title = {Cyberbullying Ends Here: Towards Robust Detection of Cyberbullying in Social Media},
  author = {Yao, Mengfan and Chelmis, Charalampos and Zois, Daphney-Stavroula},
  booktitle = {The World Wide Web Conference},
  series = {WWW '19},
  pages = {3427--3433},
  year = {2019},
  isbn = {978-1-4503-6674-8},
  url = {http://doi.acm.org/10.1145/3308558.3313462},
  doi = {10.1145/3308558.3313462},
  organization={ACM}
}

@inproceedings{chelmis2019cyberbullying,
  title = {Minority Report: Cyberbullying Prediction on Instagram},
  author = {Chelmis, Charalampos and Yao, Mengfan},
  booktitle = {The 11th ACM Conference on Web Science},
  series = {WebSci '19},
  year = {2019},
  url = {https://doi.org/10.1145/3292522.3326024},
  doi = {10.1145/3292522.3326024},
  organization={ACM}
}
``` 

### References
[1] J. Zhou, J. Chen, and J. Ye. MALSAR: Multi-tAsk Learning via StructurAl Regularization.
Arizona State University, 2012. http://www.MALSAR.org

[2] Hosseinmardi, Homa, et al. "Prediction of cyberbullying incidents in a media-based social network." Proceedings of the 2016 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining. IEEE Press, 2016.
