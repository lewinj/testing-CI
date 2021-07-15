""" 
    This is a utility module for Homework#4 in CSCI 1100 Spring 2019
    
    To use this module, first import it:

    import hw4_util

    For Part 1, use n = get_number_of_password_lists() to determine n, the number
    of password lists currently available. Then use get_password_list(num) where
    num is between 0 and n - 1 to request a specific list of passwords.

    For Part 2, use the read_zip_all() function to read the data
    on ZIP codes:

    zip_codes = hw4_util.read_zip_all()
    print(zip_codes[4108])
    
    Author: Konstantin Kuzmin
    Date: 2/19/2019

"""

import os.path
import math

files = ("password_list_top_25.txt", "password_list_top_100.txt", "10_million_password_list_top_100000.txt", "10_million_password_list_top_1000000.txt")
available = []

def get_number_of_password_lists():
    """
    Checks which files with lists of passwords are currently available.
    
    Parameters:
        None
    Return value:
        An integer which is the number of different password lists currently available.
        
    """
    count = 0
    available.clear()
    for file in files:
        if os.path.isfile(file):
            available.append(file)
            count += 1
    return count

def get_password_list(number):
    """
    Given an integer, return a specific list with common passwords.
    Make sure you call get_number_of_password_lists() before attempting
    to call get_password_list()
    
    Parameters:
        number - an integer specifying a 0-based number of the list
    Return value:
        A list of common passwords corresponding to the requested list number.
        If the list number is invalid (negative or greater than the number
        of available lists - 1), an empty list is returned.
    
    """

    try:
        with open(available[number], "r") as pass_file:
            passwords = pass_file.read().split()
    except FileNotFoundError as exc:
        return []
    except IndexError as exc:
        return []
    return passwords

    
def read_zip_all():
    i = 0
    header = []
    zip_codes = []
    zip_data = []
    skip_line = False
    # http://notebook.gaslampmedia.com/wp-content/uploads/2013/08/zip_codes_states.csv
    for line in open('zip_codes_states.csv').read().split("\n"):
        skip_line = False
        m = line.strip().replace('"', '').split(",")
        i += 1
        if i == 1:
            for val in m:
                header.append(val)
        else:
            zip_data = []
            for idx in range(0,len(m)):
                if m[idx] == '':
                    skip_line = True
                    break
                if header[idx] == "latitude" or header[idx] == "longitude":
                    val = float(m[idx])
                else:
                    val = m[idx]
                zip_data.append(val)
            if not skip_line:
                zip_codes.append(zip_data)
    return zip_codes

if __name__ == "__main__":
    zip_codes = read_zip_all()
    print(zip_codes[4108])
    
    lists_count = get_number_of_password_lists()
    # Sample a few passwords from each list
    for idx in range(lists_count):
        passwords = get_password_list(idx)
        if len(passwords) <= 10:
            print(passwords)
        else:
            print(passwords[::math.ceil(len(passwords) / 10)])
