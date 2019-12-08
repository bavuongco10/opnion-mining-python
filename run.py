#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 01:15:31 2019

@author: user
"""

import time
import pandas as pd
import numpy as np
from underthesea import sentiment
import multiprocessing

df_post = pd.read_csv('./fanpost.csv')
df_cmt = pd.read_csv('./fancmt.csv')

df_post['sentiment'] = 'None'

df_post_head = df_post.head()
df_cmt_head = df_cmt.head()

all_restaurant_name = df_post['page_name'].unique()


def parallelize_dataframe(df, func, n_cores=multiprocessing.cpu_count()):
    df_split = np.array_split(df, n_cores)
    pool = multiprocessing.Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df

def get_sentiments(df):
  for index, row in df.iterrows():
    message = row['message']
    sentiment_status = 'None'
    if not pd.isnull(message):
      sentiment_status = sentiment(message)

      df.loc[index, 'sentiment'] = sentiment_status
  return df


start = time.time()
train = parallelize_dataframe(df_post, get_sentiments)
end = time.time()
print('elapse time:', end - start)


start = time.time()
train2 = parallelize_dataframe(df_cmt, get_sentiments)
end = time.time()
print('elapse time:', end - start)






