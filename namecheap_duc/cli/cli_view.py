
import argparse, getpass
from . import cli_controller

class CLI_View():
    '''
    View object for a command line interface of Namecheap DDNS
    '''

    def __init__(self):
        pass

    # Parse command line arguements to the controller
    def parse_args(self):
        parser = argparse.ArgumentParser(description='Update a DNS A record on the Namecheap system')
        parser.add_argument('-d','--domain', help='domain to be updated')
        parser.add_argument('-p','--pass', help='DDNS password')
        parser.add_argument('--host', help='optional host to be updated')
        parser.add_argument('--address', help='optional address for DNS record')
        
        args = parser.parse_args()
        return args

    # Get domain for the user
    def get_domain(self):
        domain = input('Enter the domain to be updated: ')
        return domain

    # Get password from the user
    def get_password(self):
        passwd = getpass.getpass('Enter your DDNS password (this is not your account password): ')
        return passwd

    # Prints a generic string
    def print_string(self, string):
        print(string)

