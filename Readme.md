# To run the flask app
#### Prequsities to run the app: python3 and mysql
#### Run the command from cli python app.py.
#### If there is a data file, then the commadn is python app.py --csv <file_name>
# For the enviroment setup:
#### Make the setup script executable on MAC using chmod +x option and execute the script called script.sh
#### For windows platform, execute the script called script.bat
# For kubernetes deployments
#### Navigate to mysql-k8 and run kubectl apply -f on all the files. This will deploy mysql
#### Navigate to flask-k8 and run kubectl apply -f on all the files. This will deploy mysql
#### Although I could not finish the process of loading data to mysql, I would have done it by deploying side car containers.

