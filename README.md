<h1 align="center">Random User and Fruityvice</h1>
<h1 align="center">Data extraction and processing using APIs</h1>

<h2>Tool used:</h2>
<ul>
   <li>APIs process</li>
   <li>Python Language</li>
   <li>Spyder IDE</li>
   <li>pandas, randomuser & requests libraries</li>
</ul>

<h2>About APIs</h2>
<p>RandomUser is an open-source, free API providing developers with randomly generated users to be used as placeholders for testing purposes.</p>
<p>The API can return multiple results, as well as specify generated user details such as gender, email, image, username, address, title, first and last name, and more.</p>
<p>The required data is available using <b>randomuser</b> library</p>
<br>
<p>Another example of simple API we will use in this notebook is Fruityvice application. The Fruityvice API web service which provides data for all kinds of fruit! You can use Fruityvice to find out interesting information about fruit and educate yourself. The web service is completely free to use and contribute to.</p>
<p>The required data seems to be available on the URL: <a href="https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all">Fruityvice Data Link</a></p>


<h2>Objectives</h2>
<ul>
   <li>Load and use <b>RandomUser API</b>, using <i>RandomUser()</i> Python library</li>
   <li>Load and use <b>Fruityvice API</b>, using <i>requests</i> Python library</li>
</ul>

<h2>The Analysis</h2>
<h3>RandomUser API</h3>
<p>Generate a table with information about 10 random users with parameters such as: name, geneder, city, etc.</p>

```python
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
```
![image](https://github.com/user-attachments/assets/7f7af36e-3dbd-4a4f-acc8-83583de76f27)

<h3>Fruityvice API</h3>
<p>How many calories are contained in a banana?</p>

```python
import requests
import json

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
df2 = pd.json_normalize(results)

banana_calories = df2.loc[df2['name']=='Banana']
print("Banana calories = ", banana_calories.iloc[0]['nutritions.calories'])
```
![image](https://github.com/user-attachments/assets/2ef1d088-12d5-403a-88e5-5774ce78b3bb)

![image](https://github.com/user-attachments/assets/cef35729-8f80-4487-983e-ef51437bc4fe)

