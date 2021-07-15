"""

Hiomework 4 part 1
Is This Crazy Password Valid?
by James Lewin

The program tests the validity of a user inputed password 
based on rules defined by the instructor.

"""
import hw4_util


def rule_1(password):
    """
    The function tests rule 1:
    the password must be between 4 and 25 characters long and starts with a letter.
    """
    if len(password) <= 4 or len(password) > 25 or password[0].isalpha() == False:
        return False
    else:
        return True
    
def rule_2(password):
    """
    The function tests for rule 2:
    the password can't be in a list of common passwords (case uinsensitive).
    """
    passwords = hw4_util.get_password_list(commonlist)
    if passwords.count(password.lower()) > 0:
        return False
    else:
        return True
    
def rule_3(password):
    """
    The function checks rule 3: 
    the password must have at least one @ or $ and no %.
    """
    if password.count("%") > 0:
        return False
    elif password.count("@") > 0 or password.count("$") > 0:
        return True
    else:
        return False

def rule_4(password):
    """
    The function checks for rule 4:
    the password should have one upper case letter and one lower case letter,
    or have at least one number between 1 and 4 inclusive.
    """
    if password.islower():
        count = 0
        #Checks for 
        for i in range(1, 5):
            if password.count(str(i)) > 0:
                count += 1
        if count > 0:
            return True
        else:
            return False
    else:
        return True

def rule_5(password):
    """
    The function checks for rule 5:
    every upper case letter in the password must 
    have an underscore following it.
    """
    
    letter_upper = 0
    propper_upper = 0
    #Checks to see what characters are upper case and if a "_" follows them.
    for i in range(0, len(password)):
        if password[i].isupper():
            letter_upper += 1
            #Middle if to avoid out of range errors
            if i < len(password) - 1:
                if password[i + 1] == "_":
                    propper_upper += 1                
                    #checks to see if every upper case is followed by "_"
    if letter_upper == propper_upper:
        return True
    else: 
        return False
    
def rule_6(password):
    """
    The function chescks for rule 6:
    the should be no numerical digits greater than five.
    """
    count = 0
    for i in range(5, 10):
        if password.count(str(i)) > 0:
            count += 1
    if count > 0:
        return False
    else:
        return True
#Gives us the number of common password lists available.
lists_count = hw4_util.get_number_of_password_lists()
#The variable get info from the user.
commonlist = input("Select the list of common passwords by entering a number between 0 and {:d} => ".format(lists_count - 1))
print(commonlist)
commonlist = int(commonlist)

password = input("Enter a password => ")
print(password)

#The list is used to help check if the rules are being satisfied, and the variable is a counter.
satisfied = 0
ruleslist = [rule_1(password), rule_2(password), rule_3(password), rule_4(password), rule_5(password), rule_6(password)]

#The for loop checks if the rules are satisfied.
for i in range(0, len(ruleslist)):
    if ruleslist[i]:
        print("Rule {:d} is satisfied".format(i + 1))
        satisfied += 1
    else:
        print("Rule {:d} is not satisfied".format(i + 1))
#The if satatement formats the output based on what rules are satisfied.
if satisfied == len(ruleslist):
    print("The password is valid")
elif ruleslist[0]:
    new_password = password[:3] + "42" + password[-3:]
    print("A suggested password is: " + new_password)
else:
    print("The password is not valid")
    
    