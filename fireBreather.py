from app.functions import *

loop = True
cont = False
user_input = None


def print_menu():
    print 2 * "\n"
    print 30 * "-", "MENU", 30 * "-"
    print "1. run Fire Breather"
    print "2. change wio1_token"
    print "3. Print Variables"
    print "4. Exit"
    print 67 * "-"
    print "\n"


def print_variables():
    print 2 * "\n"
    print 30 * "-", "VARS", 30 * "-"
    print 'wio1_token: ' + wio_token
    print 67 * "-"
    raw_input("\n\nPress Enter to continue...")


while loop:
    print_menu()
    choice = input("Make an assessment: ")

    if choice == 1:
        get_temperature(wio_token)
    elif choice == 2:
        user_input = raw_input('Change wio_token : ')
        wio_token = user_input
    elif choice == 3:
        print_variables()
    elif choice == 4:
        print "Exiting Program"
        loop = False
    else:
        raw_input("Invalid option. Enter any key to try again..")
