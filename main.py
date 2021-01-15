'''
Computer Science Programming Project - Email Validator

Oliver Cordingley - 15/01/2020

Works by validating the email against a series of regular expressions
'''

# import libraries
import argparse
import re   # regular expression library

# argparse package allows terminal arguments to be parsed neatly, and makes input less of a drag to obtain
parser = argparse.ArgumentParser(description='Validates email addresses.') # Initialise our argument parser
parser.add_argument('-L', '--list', help='List of email addresses to validate') # The file name of email addresses to validate
parser.add_argument('-A', '--address', help='Email address to validate') # The email address to validate (ignored if the list argument is passed)
parser.add_argument('-q', '--quiet', help='Do not give details on why an email address was not correct', action='store_true') # Whether or not the program should just return T/F for each validated email

def validateEmail(address, quiet=False):
    # full regex:
    # /^[\w-\.\d]+@([\w-]+\.)+[\w-]{1,24}$/g
    # [\w-\.0-9]   : allow all 'sentence' letters, a-z A-Z, allow '.' and 0-9. There are many other allowed characters but these are being ignored for the sake of simplicity.
    # ([\w-\d]+\.) : allow all 'sentence' characters for first part of domain, and enforce a '.'
    # +[\w]{1,24}  : for the TLD, allow all sentence characters, with a minimum of 2 characters and a max of 24. The minimum character for a TLD is *technically* 0, however anything less than 2 is rare, and the longest TLD that exists is 24 characters

    # Match the string against our regular expression
    pattern = re.compile("^[\\w\\-\\.]+@([\\w\\-]+\\.)+[A-Za-z]{2,24}$") 
    # Test the string and convert the result to a boolean
    res = bool(pattern.match(address))

    # If the quiet flag has been passed simply just check the address string against a regular expression and return True or false
    if (quiet):
        
        # Return a stringified version of the output,
        # may end up changing as it isn't "gOoD pRaCtIcE",              I guess I could use a separate function for quiet mode? Although I don't
        # but it seems to be the easiest way to do it at                really see the point.
        # the minute because I do not want to be checking                                                      If it works, it works, I guess. :)
        # data types further down the line.
        return f"{res}" # this string interpolation requires Python3.6+
    else:
        # Check the string first, to prevent unnessecary testing
        if (res) :
            return f"{res}"

        # Split the email address into a working format
        splitaddr = address.split('@')
        if (len(splitaddr) != 2):
            return 'There must be only 1 \'@\' in an email address'
        
        # RegEx checks for the 3 main parts of the email address
        rechecks = [
            re.compile(r"^[\w\-\.]+$"),
            re.compile(r"^[\w\-]+$"),
            re.compile(r"^[A-Za-z]{2,24}$")
        ]

        if (not bool(rechecks[0].match(splitaddr[0]))):
            return 'There must only be alphanumerical characters, - and . in the first part of an email address'
        else:
            spliturl = splitaddr[1].split('.')
            # Check that the domain does infact contain a '.'
            if (len(spliturl) != 2):
                return 'You must have a valid domain name at the end of an email address'
            
            if (not bool(rechecks[1].match(spliturl[0]))):
                return 'The domain name can only contain alphanumeric characters and hyphens'

            if (not bool(rechecks[2].match(spliturl[1]))):
                return 'The TLD (domain extension, .com, .net, etc) needs to 2 or more characters and less than 25 (inclusive), and only contain letters'

        return f"{True}"

if __name__ == '__main__':
    # for now we will just check one email address without input from the user.

    print(validateEmail("hello23@iclouw24-d.cds", False))