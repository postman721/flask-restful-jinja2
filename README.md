# flask-restful-jinja2


Example api project using flask-restful and jinja2 templating. 

```
########################
#Installation and setup.
########################

#Dependencies.
###################

# sudo apt-get install -y apt-get install python3-venv python3-pip curl libgcc1-dbg

# Place api materials into folder and cd into that folder.

#Setup the virtual environment.
###############################
 
# python3 -m venv env requests
# source env/bin/activate
# pip3 install flask-restful

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

# localhost:5000/result == Once the submit button of /user endpoint is clicked there result will show in here -> Request will be redirected to this page.

```


Flask-restful api functionalities as screenshots


![1](https://user-images.githubusercontent.com/29865797/111880021-ad9e9500-89b1-11eb-8797-2f1a359f9fda.png)

![2](https://user-images.githubusercontent.com/29865797/111880023-b000ef00-89b1-11eb-83cb-c62f5ca9e17f.png)


![3](https://user-images.githubusercontent.com/29865797/111880025-b1cab280-89b1-11eb-9d71-4a6336a5b964.png)


![4](https://user-images.githubusercontent.com/29865797/111880028-b42d0c80-89b1-11eb-93fb-45757cb36384.png)


![5](https://user-images.githubusercontent.com/29865797/111880033-b68f6680-89b1-11eb-9bda-676744a91b5f.png)

