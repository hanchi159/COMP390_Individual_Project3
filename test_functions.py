import pytest
from testfixtures import TempDirectory
from print_functions import *
from util_funcs import lock_depth_positive_check

"""
This is the Automated unit test module for this project.
Unit tests are defined here for three functions defined in this project.
You can test 'print_separation_line', 'extract_msg_file_content', and 'lock_depth_positive_check' function.
"""

def test_print_separation_line(capfd):
    # test 'print_separation_line' function
    assert print_separation_line('=', 2) == '=='
    assert print_separation_line('=', 0) == ''
    assert print_separation_line('=', 10) == '=========='
    assert print_separation_line('', 2) == ''
    assert print_separation_line('=', -1) == ''

    with pytest.raises(TypeError)as error:
        print_separation_line('=', '1')
    assert error.type is TypeError

def test_extract_msg_file_content(capfd):
    # test 'extract_msg_file_content' function to print correct message.
    with TempDirectory() as tempDir:
        temp_filename = 'text.txt'
        test_line = b'SecretMessage'
        tempDir.write(temp_filename, test_line)

        file_path = tempDir.path + '\\' + temp_filename

        extract_msg_file_content(file_path)

    out, err = capfd.readouterr()
    assert out == ' -> SecretMessage\n'

    missing_file = 'missing_file.txt'
    with pytest.raises(FileNotFoundError) as file_error:
        extract_msg_file_content(missing_file)
    assert file_error.type is FileNotFoundError

def test_lock_depth_positive_check(capfd):
    # test lock_depth_positive_check function.

    assert lock_depth_positive_check(2, '2') == 2

    assert lock_depth_positive_check(0, '0') == None
    arg_val = '0'
    out, err = capfd.readouterr()
    assert out == f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0(zero).\n\n'

    assert lock_depth_positive_check(-1,'-1') == None
    arg_val = '-1'
    out, err = capfd.readouterr()
    assert out == f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0(zero).\n\n'






