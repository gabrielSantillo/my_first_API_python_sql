# importing Flask to run the server
from flask import Flask
# importing from dbhelpers the run_statement function that will handle all db connection, get the result and close the connection
from dbhelpers import run_statement
# importing json to send the API response
import json

# calling the Flask function which will return a value that I will be used for my API
app = Flask(__name__)

# making the request with this endpoint /animal and associoating if the function below
@app.get('/animal')
# function that will call the run_statement
def get_animals():
    # getting back the results of the call
    results = run_statement("CALL get_all_animals()")
    # if the result is a list, which means that the result is not None or an error
    if(type(results) == list):
        # set the result to a JSON
        animals_json = json.dumps(results, default=str)
        # return the JSON
        return animals_json
    # if the results is not a list, return a message that somenthin has gone wrong
    else:
        return "Sorry, something has gone wrong."

# making the request with this endpoint /animal and associoating if the function below
@app.get('/dog')
# function that will call the run_statement
def get_dogs():
    # getting back the results of the call
    results = run_statement("CALL get_all_dogs()")
    # if the result is a list, which means that the result is not None or an error
    if(type(results) == list):
        # set the result to a JSON
        animals_json = json.dumps(results, default=str)
        # return the JSON
        return animals_json
    # if the results is not a list, return a message that somenthin has gone wrong
    else:
        return "Sorry, something has gone wrong."

# making the request with this endpoint /animal and associoating if the function below
@app.get('/cat')
# function that will call the run_statement
def get_cats():
    # getting back the results of the call
    results = run_statement("CALL get_all_cats()")
    # if the result is a list, which means that the result is not None or an error
    if(type(results) == list):
        # set the result to a JSON
        animals_json = json.dumps(results, default=str)
        # return the JSON
        return animals_json
    # if the results is not a list, return a message that somenthin has gone wrong
    else:
        return "Sorry, something has gone wrong."

# starting our application flask server with debug mode turned on
app.run(debug=True)