#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pickle
import pandas as pd


# In[2]:


pickle_path = 'weight-prediction.model'

class MyCustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "__main__":
            module = "inference"
        return super().find_class(module, name)


# In[5]:


class PredictionModel:
    def __init__(self, encoder, model):
        self.encoder = encoder
        self.model = model
        
    def predict(self, inp):
        import numpy as np
        
        encoded_part = self.encoder.transform(inp[['Species']]).toarray()
        X = inp.drop(['Species'], axis=1)
        np.hstack([X.values, encoded_part])
        
        return self.model.predict(X)


# In[6]:

unpickler = MyCustomUnpickler(open(pickle_path, 'rb'))
model = unpickler.load()


# In[14]:


testing_sample = pd.DataFrame(
    columns=["Species", "LengthVer", "LengthDia", "LengthCro", "Height", "Width"], 
    data=[
        ['Bream', 30, 35, 38, 14, 5],
        ['Whitefish', 22, 24, 27, 7, 4]
    ])


# In[15]:

a = model.predict(testing_sample)
print(type(a))

# In[ ]:




