#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fhirclient import client
import fhirclient.models.patient as p
import fhirclient.models.bundle as bundle

settings = {'app_id':'xxxx',
            'api_base': 'https://r2.smarthealthit.org',
            'patient_id': 'smart-1137192'}
# In[2]:


settings = {'app_id': 'my-app',
            'api_base': 'https://fhir.sitenv.org/open/fhir',
            'app_secret':'my-app-secret-123',
            'launch_token': 'bXktYXBwOm15LWFwcC1zZWNyZXQtMTIz'   
            }


# In[3]:


smart = client.FHIRClient(settings=settings)


# In[4]:


#smart.ready
#smart.prepare()
#smart.ready
#smart.authorize_url


# In[5]:


patient = p.Patient.read('?_id=1&_format=json', smart.server)
patient.birthDate.isostring


# In[ ]:




