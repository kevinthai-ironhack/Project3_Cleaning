# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 09:15:57 2023

@author: monkeyluffy14
"""

import pandas as pd
import numpy as np
df = pd.read_csv('fake_jobs.csv',low_memory=False)
df.head()

sus_jobs= df[(df['requirements'].isnull()==True) & (df['required_experience'].isnull()==True) & (df['required_education'].isnull()==True) | (df['fraudulent']==1)]
sus_jobs.shape

drop_rows = list(sus_jobs.index)
df_filtered = df.drop(drop_rows, axis=0) #rows

df_teacher = df_filtered[df_filtered['title']=='English Teacher Abroad']

df_clean = pd.read_csv('dfclean.csv',low_memory=False)