# 
# Author: Jose Lo Huang
# Creation Date: 20/12/2020
# Updates:
# 21/12/2020 - Add function calls and add comments
# 
# This code is to maintain all the management menus in the same place.
# From this code, the specific Docker tasks are triggered.
# 

import Docker
import Error

error = Error.Error()

def main_menu ():
    # 
    # Main Menu:
    # This function shows the main menu and request the user option.
    # 
    print("==================================================================")
    print("DOCKER MANAGER V1.0.")
    print("1. List all containers")
    print("2. Run a container")
    print("3. Stop a container")
    print("4. Remove all stopped/exited containers")
    print("5. Run a python script on a container")
    print("6. Use docker compose")
    print("7. Exit")
    print("==================================================================")
    option = input("Please insert the number of the service you want to manage : ")
    return option


def menu ():
    # 
    # Router menu:
    # This procedure is in charge of route the user to the different docker functions
    # depending on the chosen options.
    # 
    option = None
    is_exit = 0
    docker = Docker.Docker()
    while (option != "7"):
        option = main_menu()
        print()
        # List all containers
        if (option == "1"):
            print("******************************************************************")
            print(" ALL CONTAINERS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            docker.list_containers()
        # Run container
        elif (option == "2"):
            print("******************************************************************")
            print(" RUN CONTAINER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            image = input("Please insert the image name: ")
            docker.run_container(image)
        # Stop container
        elif (option == "3"):
            print("******************************************************************")
            print(" STOP CONTAINER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            docker.stop_container()
        # Remove all stopped/exited containers
        elif (option == "4"):
            print("******************************************************************")
            print(" REMOVE CONTAINER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            docker.remove_stopped_containers()
        # Run a python script on a container
        elif (option == "5"):
            print("******************************************************************")
            print(" RUN PYTHON SCRIPT ON A CONTAINER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            docker.python_container()
        # Run a docker compose example
        elif (option == "6"):
            print("******************************************************************")
            print(" RUN DOCKER COMPOSE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
            print("******************************************************************")
            docker.docker_compose()
        # Exit program 
        elif (option == "7"):
            pass
        else:
            error.not_valid_value(option)
        print()

