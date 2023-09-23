Republic of Ireland
Munster Technological University
Department of Computer Science
Student: Jose Lo Huang

Project 2 - Docker

##################################
1. Introduction
##################################

This code is designed to execute basic administrative commands and
show the usage of Docker components, such as: images, containers and
the compose feature.

The main functions are:

1. List all containers
2. Run a container
3. Stop a container
4. Remove all stopped/exited containers
5. Run a python script on a container
6. Use docker compose

##################################
2. Code
##################################

The code included on this package is as follows:

* Docker-manager.py = Manage the main program.
* Error.py = Define the Error class and functions.
* Menus.py = Includes all the menus to trigger the docker tasks.
* Docker.py = Define the Docker class and functions.

Note: All the files must be on the same directory.

Additionally, includes the composetest subfolder for the docker
compose section with the following files:

* app.py
* requirements.txt
* Dockerfile
* docker-compose.yml

The docker compose example is from:
https://docs.docker.com/compose/gettingstarted/

2.1. How to Run 

The code was tested on Amazon Linux 2 and Mac OS Catalina with Python 3.8. 

./Docker-manager.py

Note: The option 5 of the menu can be tested using the 'test.py' file located on the directory.

2.2. Components and classes dependencies tree

+- Docker-manager.py +- Menu.py +- Docker.py +- Error.py
                                             +- composetest +- app.py
                                                            +- requirements.txt
                                                            +- Dockerfile
                                                            +- docker-composer.yml
                                                            
2.3. Menus 

2.3.1. The main menu

DOCKER MANAGER V1.0.
1. List all containers
2. Run a container
3. Stop a container
4. Remove all stopped/exited containers
5. Run a python script on a container
6. Use docker compose
7. Exit

##################################
3. Conclusion
##################################

After run this code, the user can manage the Docker container tasks in an 
efficient way. Also, it will provide an easy way to do the following 2 tasks:

* Create a container that run a python script specified by the user
* Show the functionality of docker compose

##################################
4. References 
##################################

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html
https://docker-py.readthedocs.io/en/stable/
https://docs.docker.com/engine/api/sdk/examples/
https://hub.docker.com/r/docker/whalesay/
https://www.geeksforgeeks.org/how-to-run-a-python-script-using-docker/
https://stackoverflow.com/questions/45115509/how-to-build-an-image-using-docker-api-python-client
https://www.w3resource.com/python-exercises/python-basic-exercise-2.php
https://realpython.com/python-sleep/
https://docs.docker.com/compose/install/
https://docs.docker.com/compose/gettingstarted/






