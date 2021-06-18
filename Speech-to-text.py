#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
# Importing standard libraries
import matplotlib.pyplot as plt
from ibm_watson import SpeechToTextV1
import os


# In[56]:


from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[57]:


IBM_TEXT_TO_SPEECH_API_KEY = os.enviorn.get('IBM_TEXT_TO_SPEECH_API_KEY')
IBM_TEXT_TO_SPEECH_URL = os.enviorn.get('IBM_TEXT_TO_SPEECH_URL')
api_key = IAMAuthenticator(IBM_TEXT_TO_SPEECH_API_KEY)
s2t = SpeechToTextV1(authenticator=api_key)


# In[58]:


s2t.set_service_url(IBM_TEXT_TO_SPEECH_URL)


# In[59]:


with open("myaudio.mp3", 'rb') as audio_file:
    result = s2t.recognize(
        audio=audio_file, content_type='audio/mp3'
    ).get_result()


# In[60]:


text = (result['results'])[0]['alternatives'][0]['transcript']
confidence = (result['results'])[0]['alternatives'][0]['confidence']


# In[61]:


print(f'Text obtained :- {text}')
print(f'Confidence :- {confidence}')


# In[ ]:




