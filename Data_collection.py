# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 02:20:14 2022

@author: Syeda Fatima Zahid
"""

import Glass_Door_Scrapper as gs
import pandas as pd

path = "C:/Projects/Glass door dashboard/chromedriver"





df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)