Dimensionality reduction
^^^^^^^^^^^^^^^^^^^^^^^^
The other important application of unsupervised learning is dimensionality reduction. It's mainly used for two puproses : data visualization and data compression. 

| Imagine, that you are working with high dimensional data and you want to somehow visualize data samples. As you have lots of features, your plot won't be very comprehensive and you won't get any useful insights from it. What you can do is to compress your features to just 2 or 3, thus you can easily plot them using 2D or 3D plot (that's also known as *feature projection*). 

| Now imagine that you have 30 features in your dataset and you need to train a model to classify something based on this features. First of all, using all the features available could slow down the training part a lot. Secondly, after a certain point, the performance of the model will decrease with the increasing number of elements. This phenomenon is often referred to as “The Curse of Dimensionality”. One solution, is to use usnupervised learning algorithms to reduce number of features, aggregate them.

.. note:: We haven't included feature selection techniques in this lesson, but we encourage you to read  `the article <https://towardsdatascience.com/feature-selection-techniques-in-machine-learning-with-python-f24e7da3f36e>`_  regarding it. 

Understanding PCA
=================
PCA is a technique for reducing the number of dimensions in a dataset whilst retaining most information. It is using the correlation between some dimensions and tries to provide a minimum number of variables that keeps the maximum amount of variation or information about how the original data is distributed. PCA uses mathematical techniques to reduce number of dimensions, mainly something known as the eigenvalues and eigenvectors of the data-matrix.

Understanding t-SNE
==================
t-Distributed Stochastic Neighbor Embedding (t-SNE) is another technique for dimensionality reduction and is particularly well suited for the visualization of high-dimensional datasets. Contrary to PCA it is not a mathematical technique but a probablistic one. t-SNE looks at the original data that is entered into the algorithm and seeks how to best represent this data using less dimensions by matching both distributions. The way it does this is computationally heavy and therefore there are some limitations to the use of this technique. For example one of the recommendations is that, in case of very high dimensional data, you may need to apply another dimensionality reduction technique before using t-SNE.


Description of assignment
=========================
In your last assignment in unsupervised learning section you will work with both t-SNE and PCA to reduce the dimensions of your data and visualize it effectivly. Also, you will explore a fun application of photo compression using KMeans. We hope, that you liked our course and good luck!


.. image:: https://colab.research.google.com/assets/colab-badge.svg
  :target: https://colab.research.google.com/github/HikkaV/DS-ML-Courses/blob/master/assignments/machine_learning/assignment_2_unsupervised/assignment_2.ipynb
  :width: 150
  :align: right
  :alt:  Assignment 2
