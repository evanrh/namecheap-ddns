
import requests as r
from getpass import getpass
import xml.etree.ElementTree as ET

class Requests_Client():
    '''
        Object to create a client session that updates 
        the DDNS record
    '''

    SITE_URL = 'https://dynamicdns.park-your-domain.com/update'

    def __init__(self, host=None, domain=None, passwd=None, ip_addr=None):
        self.host = host
        self.domain = domain
        self.passwd =  passwd
        self.ip_addr = ip_addr

    # Get inputs for values from the user
    def __get_inputs(self):
        
        while self.domain == None:
            self.domain = input('Enter domain to be updated: ')

        while self.passwd == None:
            self.passwd = getpass('Enter your DDNS password (this is not your account password): ')

        # Host is optional
        if self.host == None:
            self.host = input('Enter host to be updated (enter for @):')
            self.host = '@' if self.host == '' else ''

        # Defaults to public IP if none specified
        if self.ip_addr == None:
            self.ip_addr = input('Enter the IP address for the record (enter for public IP): ')

    def run(self):
        
        # Catch unentered values
        # Host is optional and only will be asked if these are not specified
        if self.domain == None or self.passwd == None:
            self.__get_inputs()

        self.__update_record()

    def __update_record(self):

        # Define site update params
        params = {'host': self.host, 'domain': self.domain, 'password': self.passwd,
                    'ip': self.ip_addr}

        # Try to post update to record
        try:
            session = r.post(SITE_URL, params=params)

        # Connection timeout
        except r.exceptions.Timeout:
            self.__update_record()

        # URL was incorrect
        except r.exceptions.TooManyRedirects:
            raise SystemExit('Error: bad url')

        # Some fatal error
        except r.exceptions.RequestException as e:
            raise SystemExit(e)

        # XML response parsing
        doc_root = ET.fromstring(session.text)
        session.close()

        errs = int(doc_root.find('ErrCount').text)

        # User introduced errors
        # Password is wrong or domain is wrong
        if errs > 0:
            for item in doc_root.find('errors'):
                print(item.text)
            raise SystemExit()

        print('DDNS Record updated successfully!')


