# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:55:33 2015

@author: sakurai
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import preprocessing


def load_data(data_name='faithful'):
    if data_name is 'faithful':
        data = np.loadtxt('datasets/faithful.txt')
        return preprocessing.scale(data)
    elif data_name is 'generate_clustering_data':
        data = generate_clustering_data.generate_clustering_data()
        return preprocessing.scale(data)
    elif data_name is 'generate_clustering_data_easy':
        data = generate_clustering_data.generate_clustering_data_easy()
        return preprocessing.scale(data)
    elif data_name is 'generate_clustering_data_tilted':
        data = generate_clustering_data.generate_clustering_data_tilted()
        return preprocessing.scale(data)
    elif data_name is 'digits':
        data = datasets.load_digits().data
        return preprocessing.scale(data)
    elif data_name is 'iris':
        data = datasets.load_iris().data
        return preprocessing.scale(data)


def generate_clustering_data():
    N, D = 100, 2
    X = []

    X_k = np.random.randn(N, D) * [50, 1] + [0, 10] + [0, -100]
    X.append(X_k)

    X_k = np.random.randn(N, D) * [50, 1] + [0, -10] + [0, -100]
    X.append(X_k)

    X_k = np.random.randn(N, D) * [1, 50] + [10, 0] + [0, 100]
    X.append(X_k)

    X_k = np.random.randn(N, D) * [1, 50] + [-10, 0] + [0, 100]
    X.append(X_k)

    return np.array(X).reshape(len(X) * N, D)


def generate_clustering_data_easy():
    N, D = 100, 2
    X = []

    X_k = np.random.randn(N, D) * [50, 1] + [0, 10] + [0, -100]
    X.append(X_k)

    X_k = np.random.randn(N, D) * [50, 1] + [0, -10] + [0, -100]
    X.append(X_k)

    return np.array(X).reshape(len(X) * N, D)


def generate_clustering_data_tilted():
    N, D = 100, 2
    X = []
    mu = np.random.randn(N, 1) * 50
    X_k = np.random.randn(N, D) + np.tile(mu, 2) + [-5, 5]
    X.append(X_k)
    mu = np.random.randn(N, 1) * 50
    X_k = np.random.randn(N, D) + np.tile(mu, 2) + [5, -5]
    X.append(X_k)
    return np.array(X).reshape(len(X) * N, D)

if __name__ == '__main__':
    X = generate_clustering_data()
    X_scaled = preprocessing.scale(X)

    plt.figure()
    plt.plot(X_scaled[:, 0], X_scaled[:, 1], '.')
    plt.show()
