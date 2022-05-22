# Fumble

### About

Fumble is an interactive online matchmaking platform. Team captains can register their teams for any sport or game and manage their team's availability for events.

They will be able to challenge other teams around the area and fight their way to the top of the leaderboards. Teams that do not come to an agreement in a challenge will be penalized and their match will be nullified.

Does your team have the skills and coordination to climb to the top?

### Python Version
Please ensure you have Python 3.8 and/or using Python 3.8. Using a newer version of Python may result in issues with the virtual environment creation.

### Setup
Download the release build, extract the zipped file, and open the folder in your preferred code editor.

### Virtual Environment
In a terminal, type the following commands to create and enable the virtual environment.

For Windows
```
python -m venv venv
.\venv\Scripts\activate
```

For Mac OS
```
python -m venv venv
source venv/bin/activate
```

### Install Project Dependencies
In a terminal, type the following commands:
```
cd Fumble_project
pip install -r requirements.txt
```

### Generating a Django Secret Key
Source Credit: https://saasitive.com/tutorial/generate-django-secret-key/

Run the following command in the terminal: 
```
python -c 'from django.core.management.utils import get_random_secret_key; \
            print(get_random_secret_key())'
```
Copy the secret key that gets generated and open the `.env` file. Now change the placeholder `INPUT_KEY_HERE` to the key you just copied. 
This step is crucial in making sure that our Django application runs correctly.

### Running the app

Make sure you are in the correct folder where the following contents are in:
```
Fumble_project
testing
website
.env
manage.py
requirements.txt
```

You will need to create your database. Type the following commands in the terminal:
```
python manage.py makemigrations
python manage.py migrate
```

Once you have completed those commands, you can start running the server with the following command:
`python manage.py runserver`

`http://127.0.0.1:PORT/` should appear in the terminal. Open the link, and you will be presented with a list of available pages.

We left debug mode on for you to view all the available pages we have in this project. Look at the next section on how to operate the website.

## Using the Website

1. First you want to create an account by going to our register page. Please note that any email will work and there was no time to implement a "forgot password" system, so make sure you enter the right password. As for the email, any email will work (it can be fake as well).
Note: It is recommended you create two users for this email to see all of our implementations!

2. Now log into one of your accounts, and create a team for them in the "Teams" page. And make sure you do the same to the other account.
3. Once, your two teams have been made, one for each user, you can now head to the challenge page.
4. Here you can choose from a list of registered teams to challenge. And make sure no two teams have a match that has the same sport twice.
5. After doing that, if you head to the home page, you can see a display of the match you just created. You can either accept or deny the match request. If you and the other team captain accepted the match, then home will display that match as "in-progress".

Hope you enjoy the web app! Our team may continue working on this after the semester to use as practice or learn more about what could of been done during the semester.

- The Fumble Team
