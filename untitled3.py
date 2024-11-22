# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k8RFhRtOzEITkNFPia4XKqGvHpFg84x1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/Fashion_Retail_Sales.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())

df

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(500, 200))
sns.histplot(df['Date Purchase'], kde=True, color='green')
plt.title('Date Purchase distribution')
plt.xlabel('Date Purchase')
plt.ylabel('Frequency')
plt.show()

sns.boxplot(df['Review Rating'])
plt.title('Popular payment method (Boxplot)')
plt.show()
plt.figure(figsize=(50, 20))
plt.hist(x=df['Item Purchased'])

plt.figure(figsize=(5, 5))
plt.hist(x=df['Payment Method'])





plt.figure(figsize=(50, 10))
sns.scatterplot(x='Item Purchased', y='Review Rating', data=df, color='purple')
plt.title('Item vs Review')
plt.xlabel('Item Purchased')
plt.ylabel('Review Rating')
plt.show()

plt.figure(figsize=(50, 10))
sns.scatterplot(x='Item Purchased', y='Customer Reference ID', data=df, color='purple')
plt.title('Item vs Customer interested in item')
plt.xlabel('Item Purchased')
plt.ylabel('Customer Reference ID')
plt.show()

df['Payment Method'].value_counts().plot(kind='pie',autopct='%.2f')





from sklearn.preprocessing import MinMaxScaler, StandardScaler


