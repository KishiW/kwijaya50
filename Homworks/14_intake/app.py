# Kishi "wawa" Wijaya
# Hungry
# SoftDev
# October 2024

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

import testmod0

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will not. 

TASK:
 Predict which.
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''



@app.route("/", methods=['GET'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***") # Empty Dictionary
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    # print(request.args['username']) # this will cause an error if the username value doesn't exist
    # print("***DIAG: request.headers ***")
    # print(request.headers)
    return render_template( 'login.html' ) # should work if login.html exists


@app.route("/auth", methods=['GET'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")# Dictionary now has username in it
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***") 
    print(request.args['username']) # Will work as we input a username in the disp_loginpage function
    print("***DIAG: request.headers ***")
    print(request.headers)
    return request.args['username']  #response to a form submission - the function will work but will not yet display username 


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
