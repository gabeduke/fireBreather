from app.functions import *

loop = True
cont = False
user_input = None


def print_menu():
    print 2 * "\n"
    print 30 * "-", "MENU", 30 * "-"
    print "1. run Fire Breather"
    print "2. change wio1_token"
    print "6. Print Variables"
    print "7. Exit"
    print 67 * "-"
    print "\n"


def print_variables():
    print 2 * "\n"
    print 30 * "-", "VARS", 30 * "-"
    print 'wio1_token: ' + wio1_token
    print 67 * "-"


while loop:
    if cont:
        print_variables()
    cont = True
    print_menu()
    choice = input("Make an assessment: ")

    if choice == 1:
        get_wio_sensor_data()
    elif choice == 2:
        user_input = raw_input('Change wio1_token : ')
        wio1_token = user_input
    elif choice == 3:
        print_variables()
    elif choice == 4:
        print "Exiting Program"
        loop = False
    else:
        raw_input("Invalid option. Enter any key to try again..")
