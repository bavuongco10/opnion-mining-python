#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 02:34:38 2019

@author: user
"""

import pandas as pd

df = pd.read_csv('./cmt_sentiment_strip_comment.csv')

df = df.sample(frac=1).reset_index(drop=True)

df.to_csv('./cmt_sentiment_strip_comment.csv')