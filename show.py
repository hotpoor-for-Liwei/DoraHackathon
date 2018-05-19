# -*- coding: utf-8 -*-
import jieba
import json


# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)
