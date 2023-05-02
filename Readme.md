## To run the flask app
# Prequsities to run the app: python3 and mysql
# Run the command from cli python app.py.
# If there is a data file, then the commadn is python app.py --csv <file_name>
## For the enviroment setup:
# Make the setup script executable using chmod +x option and execute the script
# For windows platform, the script can be executed from git bash or cygwin.
## For kubernetes deployments
# Navigate to mysql-k8 and run kubectl apply -f on all the files. This will deploy mysql
# Navigate to flask-k8 and run kubectl apply -f on all the files. This will deploy mysql
# Although I could not finish the process of loading data to mysql, I would have done it by deploying side car containers.

