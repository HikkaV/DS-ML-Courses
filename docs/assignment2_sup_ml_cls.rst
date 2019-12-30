Hyperparameters tunning
^^^^^^^^^^^^^^^^^^^^^^^
Tuning model's parameters is a very tedious and fragile work. Different algorithms have different sensitivity for different hyperparameters, that's why in order to get pick nice tunable parameters, the one need to investigate the "black box" of the algorithm, meaning it's implementation. But sometimes we just don't have enough time to make it. Suppose that you started working with some algorithm for the first time and based on it you should provide a nice solution in two days. Two days is not an enough term to understand all the subtleties of a new algorithm. What should the one do in this situation? Fortunately, the one can just try the variety of different hyperparameters and then choose the best ones.

Grid search
===========

One option is to use an exhaustive grid search which generates candidates (hyperparameters) from a grid of parameter values specified beforehand. It's very easy to understand it, but it's not very useful for a large amount of data with lots of features.

Randomized parameter optimization
=================================

Instead of iterating through the entire parameters' space, randomized search samples candidates from a distribution over possible parameter values. Two main benefits of it are the following :

* A budget (by budget we mean computational time and power) can be chosen independent of the number of parameters and possible values.
* Adding parameters that do not influence the performance does not decrease efficiency.

Tuning through minimization
===========================

The other interesting idea is to think about hyperparameters tuning as about the other optimization problem. By stating the problem that way, we can apply another algorithm (for example forest minimize) on top of ours to find the best hyperparameters by minimizing loss or maximizing accuracy/recall/etc. This solution is known to be much more precise than the two exposed before. The main benefits of this approach are the following :

* It's computationally efficient, as the search of hyperparameters is done by the learning algorithm, and thus nice values can be found much faster.
* With each iteration, the algorithm "on top" is supposed to find the hyperparameters which make the perfomance of the algorithm better, whereas random an exhaustive search can never find the best one.

.. note:: We won't consider tunning through minimization and randomize parameter optimization, but if you are interested you can learn about them `here <https://scikit-optimize.github.io/>`_ and `here <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html>`_. 

Anyway it's benefitial to have an idea about in which space to seek for best hyperparameters, as it can speed up the process of hyperparameters tunning. 


Description of assignment
=========================
For today, you will continue working with the dataset from kaggle. You will have a change to observe the lift in kaggle score after applying hyperparameters tunning and making a new feature. Good luck!

.. image:: https://colab.research.google.com/assets/colab-badge.svg
  :target: https://colab.research.google.com/github/HikkaV/VNTU-ML-Courses/blob/master/assignments/machine_learning/assignment_2_classification/assignment_2.ipynb
  :width: 150
  :align: right
  :alt:  Assignment 2