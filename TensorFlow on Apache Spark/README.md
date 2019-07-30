# TensorFlow on Apache Spark

https://databricks.com/blog/2016/01/25/deep-learning-with-apache-spark-and-tensorflow.html

Here is a quick demonstration on how to use TensorFlow and Spark together to train and apply deep learning models.
There are two main use cases for a Spark cluster to improve deep learning pipelines.

1. *Hyperparameter tuning* - to find the best set of hyperparameters for neural network training
2. *Deploying models at scale* - to apply a trained neural network model on a large amount of data

## Hyperparameter Tuning

TensorFlow library enables creation of ANNs, however there is typically a number of important hyper-parameters which need to be set.
These hyper-parameters affect the performance of the trained models and therefore need to be optimized 
by rerunning the same model multiple times with different hyper-parameters to find the best set.
This is known as hyper-parameter tuning.
This process is “embarrassingly parallel” and can be distributed using Spark.
Spark can be used to broadcast common elements, like data and model description, and then schedule individual computations across the cluster.

## Deploying Models at Scale

TensorFlow models can be embedded on pipelines to perform complex recognition tasks on datasets.
