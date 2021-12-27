#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests

url = "https://car-data.p.rapidapi.com/cars"

for year in range(2000, 2010):
    print("Year:", year)
    year = str(year)

    querystring = {"limit":"10","page":"0","year":year}

    headers = {
        'x-rapidapi-host': "car-data.p.rapidapi.com",
        'x-rapidapi-key': "22a616dc46mshc13187abbffb695p164a47jsnd0995d8c3337"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    print("..... Copying to the file ....")
    text_file = open("C:\\Users\Praveen Attaluri\Desktop\Sample\Data1.txt", "a")
    text_file.write(response.text)
    text_file.write("\n")
    text_file.close()
    print("..... Done .....")


# In[ ]:




