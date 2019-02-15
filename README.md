# CyberBullying Prediction On Instagram
Fixed-Lag Varing-Horizon (FLVH) and Fixed-Horizon Varing-Lag (FHVL) models are provided in this project. 

### Prerequisites
#### Matlab
```MALSAR[1]```
#### Python 2
```
NLTK
vaderSentiment
SKlearn
Pandas
```
### Dataset
We use comments spanning 22.1 of all media sessions containing 40% profanities from the Instagram dataset available by [2]. 10k comments have been manually annotated by 10 experts.

### How to use
In each model folder, there are the following files available:
``` raw_text_labeled.csv: a sample labeled dataset
    create_tasks.py: create tasks for multi-task learning
    train_test.py: create training and testing data
    mtl.mat: find the optimize W using MALSAR and save W matrix as a csv file
    load.mat: load W from the csv file
    mtl_regression.py: for prediciton  
```

### References
[1] J. Zhou, J. Chen, and J. Ye. MALSAR: Multi-tAsk Learning via StructurAl Regularization.
Arizona State University, 2012. http://www.MALSAR.org

[2] Hosseinmardi, Homa, et al. "Prediction of cyberbullying incidents in a media-based social network." Proceedings of the 2016 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining. IEEE Press, 2016.
