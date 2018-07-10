# coding=utf-8
import sys
import easyIO as io
import terminal_commands as terminal

menu_1 = ["Sign in", "New user"]
menu_2 = ["Input weight", "View weight", "Exit"]
message_1 = "Welcome to the Helth Tracker. Please select one of the following options."
message_2 = "Hello [Name]."                                                                 #need to change [name] to account name once accounts have been created

def main():
    menu_one()
    #menu_two()

def menu_one():
    while True:
        user_choice = io.get_user_menu_selection(title = "Please select from the following options", menu = menu_1)
        if user_choice == 0:
            print "Credentials"
            #accounts=terminal.ls(pattern="*.txt")
            #print accounts                                                                 #list existing accounts OR say there are no existing accounts
            break
        elif user_choice == 1:
            print "blablabla"                                                               #set up an account (asking for name) and creating a .txt file
            break
        else: pass

def menu_two():
    print message_2
    user_choice = 0
    while user_choice != 2:
        user_choice = io.get_user_menu_selection(title = "How can we help you today?", menu = menu_2)
        if user_choice == 0:
            weight = weight_input()
        elif user_choice == 1:                                                              #need to input graph visual on long term
            print "Do this bit later"
        else: pass
    sys.exit()

def weight_input():                                                                         #change it to an array that is fed into python file at start and then append new entries when exiting
    user_weight = io.get_user_input(message = "Please input your weight: ", dtype = float)
    # Create file to write into
    output_file = open("name1.txt", "a+")
    # Write to the file
    output_file.write("{:4.1f}".format(user_weight))
    output_file.write("\n")
    output_file.close()

main()
