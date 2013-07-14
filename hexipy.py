"""Program that will ask for hex translactions and you have to enter the answer

Example Questions:

Options:
Hex to Bin
Bin to Hex
Dec to Hex
Hex to Dec

"""
from random import randint
import sys

ONE_TO_ONE = 1
RANDOM = 2
EXIT = 3
CHAR_EXIT = ['x','X','exit','EXIT']

HEX = 'h'
BIN = 'b'
DEC = 'd'

mode_opts = {ONE_TO_ONE:"One-to-One",
             RANDOM:"Random",
             EXIT:"Exit"}

hex_opts = {HEX:'hex',
            BIN:'bin',
            DEC:'dec'}

hex_values = {}
hex_values[0] = {HEX:'A',BIN:'1010',DEC:'10'}
hex_values[1] = {HEX:'B',BIN:'1011',DEC:'11'}
hex_values[2] = {HEX:'C',BIN:'1100',DEC:'12'}
hex_values[3] = {HEX:'D',BIN:'1101',DEC:'13'}
hex_values[4] = {HEX:'E',BIN:'1110',DEC:'14'}
hex_values[5] = {HEX:'F',BIN:'1111',DEC:'15'}

#Example Hex to Bin:
class UserOpts(object):
    mode = None
    frm_unit = None 
    to_unit = None

    @staticmethod
    def print_opts():
        print "Mode:",UserOpts.mode
        print "from Unit",UserOpts.frm_unit
        print "to unit",UserOpts.to_unit

#print "What is %s from %s to %s? " % (hex_values[0][frm], opts[frm], opts[to])

def exit(rc):
    print "Termination requested. Exiting."
    raise SystemExit(0)

def change_frm_to():
    print "----------------------------"
    print " Choose Conversion Options"
    print "----------------------------"
    for opt in hex_opts:
        print " ('%s') %s" % (opt, hex_opts[opt])
    print ""

    def get_frm():
        sys.stdout.write("Convert From: ")
        frm_choice = raw_input()

        if frm_choice not in hex_opts:
            print "Invalid option selected."
            get_frm()
        else:
            UserOpts.frm_unit = frm_choice

    def get_to():
        sys.stdout.write("        To:   ")
        to_choice = raw_input()

        if to_choice not in hex_opts:
            print "Invalid option selected."
            get_to()
        elif to_choice == UserOpts.frm_unit:
            print "To Choice cannot match From Choice"
            get_to()
        else:
            global to_unit
            UserOpts.to_unit = to_choice

    get_frm()
    get_to()

def change_mode():
    """Prompts user to change the mode"""

    print "---------------"
    print " Mode Options:"
    print "---------------"

    for mode in mode_opts:
        print " (%d) %s" % (mode, mode_opts[mode])

    sys.stdout.write("\nChoose mode: ")
    user_choice = raw_input()
    
    try:
        user_choice = int(user_choice)

        if user_choice not in mode_opts:
            print "Error: Please choose a valid option."
            print "--------"
            change_mode()
        elif user_choice == EXIT:
            exit(0)
        else: 
            #global mode
            UserOpts.mode = user_choice
            print "Mode is set to", mode_opts[mode]

            if UserOpts.mode == 1:
                """Need to askwhat to change from to"""
                change_frm_to()
            elif UserOpts.mode == 2:
                frm = None
                to = None
            else:
                print "Invalid Mode detected. Exiting."
                exit(0)
    except SystemExit:
        pass
    except:
        print "Error: Invalid input. Only input numbers"
        print "--------"
        change_mode()

class ChangeModeRequest(Exception):
    def __init__(self):
        Exception.__init__(self)

def start_one_to_one_mode():
    while True:
        hex_val = randint(0,len(hex_values)- 1)

        print "What is %s, from %s to %s" % (hex_values[hex_val][UserOpts.frm_unit], hex_opts[UserOpts.frm_unit], hex_opts[UserOpts.to_unit])

        user_answer = raw_input()

        if user_answer == hex_values[hex_val][UserOpts.to_unit]:
            print "Correct"
        elif user_answer in CHAR_EXIT:
            exit(0)
        else:
            print "Incorrect"

        print "---------------------------------"

def start_random_mode():
    """Choose random conversion, and random hex value"""
    while True:
        hex_val = randint(0, len(hex_values) - 1)

        #Need to choose a random index, but since hex_opts keys are letters ths makes it difficult
        #Get a random index from hex_opts.keys() and then get its associated val
        rand_frm_idx = randint(0, len(hex_opts.keys()) - 1)
        rand_frm = hex_opts.keys()[rand_frm_idx]

        #Same logic as rand_frm, but need to create a new list deleting rand_frm, so that we dont have a type to same type request.
        to_hex_opts = hex_opts.keys()
        del(to_hex_opts[rand_frm_idx])

        rand_to_idx = randint(0, len(to_hex_opts) - 1)
        rand_to = to_hex_opts[rand_to_idx]

        print "What is %s, from %s to %s" % (hex_values[hex_val][rand_frm], hex_opts[rand_frm], hex_opts[rand_to])

        user_answer = raw_input().upper()
        correct_answer = hex_values[hex_val][rand_to]

        if user_answer == correct_answer:
            print "Correct"
        elif user_answer in CHAR_EXIT:
            exit(0)
        else:
            print "Incorrect. Right Answer:", correct_answer

        print "---------------------------------"

if __name__ == "__main__":
    print "Welcome to Hexifpy"
    change_mode()
    print "Starting. Press 'x' at any point to exit"
    
    if UserOpts.mode == ONE_TO_ONE:
        start_one_to_one_mode()
    elif UserOpts.mode == RANDOM:
        start_random_mode()
    else:
        print "Invalid mode found. Mode",UserOpts.mode
        exit(1)

