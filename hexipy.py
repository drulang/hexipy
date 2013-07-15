help = """
NAME
    hexipy -- Learning tool to test and strengthen your hexadecimal conversion 

DESCRIPTION
    Hex values are chosen at random and prompts the user to convert the value from/to any combination of hexadecimal, binary, or decimal.

    -h Print this and exit

MODE
    1. One-to-one : User chooses what units to use for conversion
    2. Random     : From/To conversions are chosen at random
    3. Exit       : Program exits
 
RUNTIME CMD
    x : Exit Program

"""
from random import randint
import sys

ONE_TO_ONE = 1
RANDOM = 2
EXIT = 3
CHAR_EXIT = ['q','Q','quit','QUIT','x','X','exit','EXIT']

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

class UserOpts(object):
    mode = None
    frm_unit = None 
    to_unit = None

    @staticmethod
    def print_opts():
        print "Mode:",UserOpts.mode
        print "from Unit",UserOpts.frm_unit
        print "to unit",UserOpts.to_unit

def exit(rc):
    print "Termination requested. Exiting."
    raise SystemExit(0)

def change_frm_to():
    """
    Print menu that allows a user to change the
    From and To conversion options
    """

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
    """Menu that allows the user to change the mode
       of the program"""

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
            UserOpts.mode = user_choice
            print "Mode is set to", mode_opts[UserOpts.mode]

            if UserOpts.mode == 1:
                """Need to askwhat to change from to"""
                change_frm_to()
            elif UserOpts.mode == 2:
                UserOpts.from_unit = None
                UserOpts.to_unit = None
            else:
                print "Invalid Mode detected. Exiting."
                exit(0)
    except SystemExit:
        pass
    except:
        print "Error: Invalid input. Only input numbers"
        print "--------"
        change_mode()

def start_one_to_one_mode():
    while True:
        hex_val = randint(0,len(hex_values)- 1)

        print "What is %s, from %s to %s" % (hex_values[hex_val][UserOpts.frm_unit], hex_opts[UserOpts.frm_unit], hex_opts[UserOpts.to_unit])

        user_answer = raw_input().upper()
        correct_answer = hex_values[hex_val][UserOpts.to_unit];

        if user_answer == correct_answer:
            print "Correct"
        elif user_answer in CHAR_EXIT:
            exit(0)
        elif user_answer == 'M':
            main_menu()
        else:
            print "Incorrect. Correct answer:", correct_answer

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
        elif user_answer == 'M':
            main_menu()
        else:
            print "Incorrect. Right Answer:", correct_answer

        print "------------------------------"

def main_menu():
    change_mode()
    print "------------"
    print "Starting.\n Press 'x' to exit"
    print "------------"
    
    if UserOpts.mode == ONE_TO_ONE:
        start_one_to_one_mode()
    elif UserOpts.mode == RANDOM:
        start_random_mode()
    else:
        print "Invalid mode found. Mode",UserOpts.mode
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            print help
            sys.exit(0)

    print "Welcome to Hexipy"
    main_menu()

