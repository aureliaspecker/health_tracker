# coding=utf-8
import sys
import easyIO as io
import terminal_commands as terminal

menu_1 = ["New account", "Account1", "Account2"]
menu_2 = ["Input weight", "View weight", "Exit"]
message_1 = "Welcome to the Helth Tracker. Please select one of the following options."
message_2 = "Hello [name]."                                                                 #need to change [name] to account name once accounts have been created

def main():
    print message_2
    user_choice = io.get_user_menu_selection(title = "How can we help you today?", menu = menu_2)
    if user_choice == 0:
        weight = weight_input()
    elif user_choice == 1:
        print "hello option 2"
    elif user_choice == 2:
        print "hello option 3"
        sys.exit()

def weight_input():
    print "test: calls function weight_input()"
    user_weight = io.get_user_input(message = "Please input your weight", dtype = float)    #THIS DOESN'T WORK
    return user_weight


# def main():
#     # user_input=io.get_user_input(message="Enter input: ",dtype="float")
#     # print user_input
#     #
#     # menuuuuu=["option a","option b", "option c"]
#     # user_input=io.get_user_menu_selection(title="Main menu",menu=menuuuuu)
#     # print user_input
#     #
#     # existing_profiles=terminal.ls(pattern=".*.dat")
#     # print existing_profiles


main()
