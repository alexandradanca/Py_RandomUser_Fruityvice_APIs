#### RandomUser API
#!pip install randomuser
from randomuser import RandomUser
import pandas as pd

r = RandomUser()
user_list = r.generate_users(10)

def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)

df1 = pd.DataFrame(get_users())

#### Fruityvice API
import requests
import json

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
df2 = pd.json_normalize(results)

banana_calories = df2.loc[df2['name']=='Banana']
print("Banana calories = ", banana_calories.iloc[0]['nutritions.calories'])
