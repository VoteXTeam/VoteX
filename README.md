# VoteX
## basic install
//*install latest postgresql from https://www.postgresql.org/download/
//postgresql database name votex, user postgres (default root), pass votex

//(no additional components needed after install)
//*set up python environment (I used Python 3.11)
# //install packages:
// if psycopg2 doesn't work, use psycopg2-binary
## //install pip packages (run from root folder):
pip install django psycopg2 axios django-multiselectfield django-debug-toolbar djangorestframework django_bootstrap5

## //create scripts to sync models from models.py to postgresql (if changes was made) (from root)
//terminal (C:\projects\VoteX)
python .\manage.py makemigrations

## //(create tables) sync migrations created in previous step to postgresql (from root)
python .\manage.py migrate
## //npm to install all modules (run from VoteXFront):
npm install bootstrap axios webpack webpack-cli @babel/core babel-loader @babel/preset-env @babel/preset-react react react-dom@5 @mui/material @emotion/react @emotion/styled @mui/icons-material @babel/plugin-proposal-class-properties react-router-dom browser-sync browser-sync-webpack-plugin --save-dev

## starting program
//from root VoteX directory run
python .\manage.py runserver

//open another terminal
//then cd into VoteXFront and run
npm run dev

//connect to localhost:3000 from browser (for browser reload)
//or to localhost:8000 (django)

//edit App.js or any other file and press Ctrl + S to update browser


//Structure:
//VoteX floder is a core app, used to manage server and settings
//VoteXApi is an app for back-end configuration
//VoteXFront is React app for front-end development
//Main React file = VoteXFront/src/components/App.js


## NOTES
//needed pip packages
pip install django
//postgreSQL connection
pip install psycopg2
//toolbar for checking queries to database (top right button)
pip install django-debug-toolbar
//django rest
pip install djangorestframework

//install bootstrap5
pip install django_bootstrap5

//terminal (C:\projects\VoteX)
//create scripts to sync models from models.py to postgresql (if changes was made)
python .\manage.py makemigrations

//(create tables) sync migrations created in previous step to postgresql
python .\manage.py migrate

//needed node_modules
//CD INTO "VoteXFront"!


//how to start
//from root VoteX directory run
python .\manage.py runserver

//then cd into VoteXFront and run
npm run dev

//connect to localhost:3000 from browser (for browser reload)
//or to localhost:8000 (django)

//edit App.js or any other file and press Ctrl + S to update browser

//Structure:
//VoteX folder is a core app, used to manage server and settings
//VoteXApi is an app for back-end configuration
//VoteXFront is React app for front-end development
//Main React file = VoteXFront/src/components/App.js


//install webpack
//From "VoteX/VoteXFront":
npm install webpack
npm i webpack-cli --save-dev

//convert for older browsers
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev

//install react
npm i react react-dom --save-dev

//install material-ui (smthing like bootstrap)
npm install @mui/material @emotion/react @emotion/styled
npm install @mui/icons-material

//install async and await to js
npm install @babel/plugin-proposal-class-properties

//install react-router-dom to reroute the pages
npm install react-router-dom

//install browser-sync for auto reloads
npm install --save-dev browser-sync
npm install --save-dev browser-sync-webpack-plugin

