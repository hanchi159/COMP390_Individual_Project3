import sys
import print_functions
import command_functions

"""
This is jlock main function module.
Main function runs here and get command.
"""

def parse_command_line_args(arg_list):
    # Check the command line argument and call command functions.

    if len(arg_list) == 1:
        print_functions.print_welcome_message()

    elif len(arg_list) == 2:
        command = arg_list[1]
        if command == '-help' or command == '-h':
            command_functions.help_command()

        elif command == '-msg':
            command_functions.msg_command()

        elif command == '-locked':
            command_functions.locked_command()

        elif command == '-clear':
            command_functions.clear_command()

        else:
            print('Error: invalid command')

    elif len(arg_list) == 3:
        if arg_list[1] == '-unlock':
            command_functions.unlock_command(arg_list)
        else:
            print('Error: invalid command')

    elif len(arg_list) == 4:
        if arg_list[1] == '-lock':
            command_functions.lock_command(arg_list)
        else:
            print('Error: invalid command')

    else:
        print('Error: invalid command')

def jlock_main():
    # This is the main function of the project and get command line argument.
    # Insert the argument to 'parse_command_line_args(arg_list)' function.

    # get command line arguments
    arg_list = sys.argv
    # arg_list_len = len(arg_list)

    # check for empty string in command line args - empty strings are invalid input
    if '' in arg_list:
        print('Error: invalid command')
        return

    parse_command_line_args(arg_list)

if __name__ == '__main__':
    jlock_main()
