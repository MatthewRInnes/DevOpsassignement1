weight converter

this is a flask app for converting weight between kg grams and pounds

to run it you need to make a venv first, then install the requirements
python -m venv venv
then activate it (on windows its venv\Scripts\activate)
pip install -r requirements.txt
then run the app with python app.py

for tests just run pytest -v in the flask-app directory

I did this for the devops lab, it was a bit confussing at first but it works now
# 1. Go to the folder YOU care about
cd "C:\Users\matth\Desktop\DevOpsassignement1-main"

# 2. Turn it into a git repo
git init

# 3. Point it at your GitHub repo
git remote add origin https://github.com/MatthewRInnes/DevOpsassignement1.git

# 4. Stage and commit EVERYTHING in this folder
git add .
git commit -m "Initial commit from DevOpsassignement1-main project"

# 5. Make sure the branch is called main
git branch -M main

# 6. Push it to GitHub, replacing what is there
git push -u origin main --force