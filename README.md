# Blog-Built-with-Django


### This is part of the `Zuri x I4G Training` task 

A Beginner Training For Complete Tech Novices Or Beginners

Am on the Back End Track specifically Python #Be-Python

```python
import os
from decouple import config

from pathlib import Path

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
       
```

## Task

Create a `Register Page` (a new user can register, their details stored in a database file). 

-    `Login` (checks in the file and logs them in if they are already registered)

-    `Reset Password`

-    `Logout`

-    A `comment section`, you must be logged in to comment

-    Host the project on `Heroku`


Connect with me on these platforms:

<a href="https://twitter.com/Blestseun"><img src="https://res.cloudinary.com/kolaisaac10/image/upload/v1598833526/samples/Social%20Site/twitter1_jtffso.png" alt="Twitter Link" width="120" height="45" /> </a>
<a href="https://www.linkedin.com/in/kolaisaac10/"><img src="https://res.cloudinary.com/kolaisaac10/image/upload/v1598828481/samples/Social%20Site/linkedIn_kgfq3n.png" alt="LinkedIn Link" width="120" height="45"/>
<a href="https://www.youtube.com/channel/UCqkUuiGggw2jptTa6piUiQQ"><img src="http://res.cloudinary.com/kolaisaac10/image/upload/v1598828481/samples/Social%20Site/YouTube_colah1.png" alt="YouTube Link" width="120" height="45" /> </a> 
<a href="https://medium.com/@BlestIsaac"><img src="https://res.cloudinary.com/kolaisaac10/image/upload/v1598833526/samples/Social%20Site/medium1_brliej.png" alt="Medium Link" width="120" height="45" />
<a href="https://www.kaggle.com/kolaisaac10"><img src="https://res.cloudinary.com/kolaisaac10/image/upload/v1598833035/samples/Social%20Site/kaggle2_lgioik.png" alt="Kaggle Link" width="120" height="45" />
<a href="https://zindi.africa/users/Sir-isaac"><img src="https://res.cloudinary.com/kolaisaac10/image/upload/v1598828481/samples/Social%20Site/zindi_jntzxw.png" alt="Zindi Link" width="120" height="45" /> </a>

- 🌱 I’m always learning, I formed #DL3 (Dedicated Life Long Learner)

- 💬 Ask me about: Cloud Computing, Machine Learning and Data Science
