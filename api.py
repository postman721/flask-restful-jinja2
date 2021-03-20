
########################
#Installation and setup.
########################

#Dependencies.
###################

# sudo apt-get install -y apt-get install python3-venv python3-pip curl libgcc1-dbg

# Place api materials into folder and cd into that folder.

#Setup the virtual environment.
###############################
 
# python3 -m venv env 
# source env/bin/activate
# pip3 install flask flask-restful requests

#Run the api.py.
####################

# python3 api.py


####################
#Endpoints
#####################

# localhost:5000 == Hello World.

# localhost:5000/distributions == Distribution list.

# localhost:5000/ubuntus == Ubuntu list.

#########################
#Jinja2 templating
#########################

# localhost:5000/user == A form, which accepts 3 entries and then appends them to already defined list of entries.

# localhost:5000/result == Once the submit button of /user endpoint is clicked result will be show in here 
#-> User will be redirected to this page.


###################################
#The api.py
##################################

#Import the needed stuff.
from flask import Flask, jsonify, make_response, redirect, request, render_template
from flask_restful import Resource, Api
import requests

#Define app as Flask and then start Restful api as api.
app = Flask(__name__)
api = Api(app)

#Define classes with their request types (post,get etc.) 
#Notice how there is always (Resource) in the class definition - coming from flask-restrful.

class Hello(Resource):
    def get(self):
        return 'Hello World'

class Distributions(Resource):
    def get(self):
        return 'Debian Gnu/Linux, Gentoo , Arch Linux, SliTaz, Linux from Scratch, Fedora, Centos 8-Steam, BunsenLabs, Lubuntu, Xubuntu, Scientific Linux'

#Standard flask path with decorator and allowed methods. Also making a json out of an array here - with jsonify.
    @app.route("/ubuntus", methods=["POST", "GET"])
    def ubuntus():
        x= ['Ubuntu, Lubuntu, Xubuntu, Edubuntu, Kubuntu'] 
        return  jsonify(x) 

#############
#Jinja2
##############

#Getting the data form and appending user input to jinja2 template file

#Here we render the data form template. See inside the template folder.
#Notice that action.html has some default values in it. 

#Once we go into /user we will see the form and it will allow us to input three values. 
#These values will be joinded to the default values of action.html. 
#Once we have pressed the submit button we should be directed to /result endpoint -> action.html will post to /result endpoint and we will get redirected + see the result. 

@app.route('/user',methods = ['POST', 'GET'])
def user():
   return render_template('action.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("user_action.html",result = result)


                 
api.add_resource(Hello, '/')
api.add_resource(Distributions, '/distributions')

if __name__ == '__main__':
    app.run(debug=True)
