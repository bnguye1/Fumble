# Fumble

### About

Fumble is an interactive online matchmaking platform. Team captains can register their teams for any sport or game and manage their team's availability for events.

They will be able to challenge other teams around the area and fight their way to the top of the leaderboards. Teams that do not come to an agreement in a challenge will be penalized and their match will be nullified.

Does your team have the skills and coordination to climb to the top?

### Setup

**Note: Replace PATH with the rest of the path on your system**

1. Clone this repository

3. In PyCharm, do the following:

   1. Go to File -> Settings -> Language & Frameworks -> Django
   2. Check the "Enable Django Support"
   3. Enter this for the project root: *PATH*\Fumble\Fumble_project
   4. The other fields should detect automatically, if not:
   
      1. Settings: *PATH*\Fumble\Fumble_project\Fumble_project\settings.py 
      2. Manage Script: *PATH*\Fumble\Fumble_project\manage.py
      
4. Ensure you have a valid Python interpreter ready
   1. File -> Settings -> Project:Fumble -> Project Interpreter
   2. Hit the triple dots and select "Add"
   3. Select "Virtualenv Environment"
   4. Select this project's venv folder
   
5. In the top right, select "Add Configuration"
6. Hit the "+" and select Django server
7. Enter "127.0.0.1" into the host field
8. For the Python interpreter, it should be selected by default, if not:
   1. Select the interpreter you made earlier

### Enable Virtual Environment

In the terminal, type the following in: `.\venv\Scripts\activate` to enable venv.

### Running the app

You should be able to hit run in the top right, and a terminal should open showing some information.

`http://127.0.0.1:PORT/` should appear in the terminal. Ctrl+Click it and see if you are able to see the site.

**Note: You will see a "Page not found" upon opening the link, but you should be able to visit the different pages shown on the page.**
