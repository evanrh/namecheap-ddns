
import urllib.parse as parser
import http.client
from getpass import getpass
import xml.etree.ElementTree as ET
import socket

class No_Reqs_Client():
    '''
        Object to create a client session that updates 
        the DDNS record
    '''

    SITE_URL = 'dynamicdns.park-your-domain.com'
    PATH = '/update'

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

        queries = parser.urlencode(params)
        # Try to post update to record
        try:
            session = http.client.HTTPSConnection(self.SITE_URL)
            session.request('POST', self.PATH + '?' + queries)

        except http.client.HTTPException as e:
            raise SystemExit(e)

        response = session.getresponse()
        data = response.read()

        # XML response parsing
        doc_root = ET.fromstring(data)
        session.close()

        errs = int(doc_root.find('ErrCount').text)

        # User introduced errors
        # Password is wrong or domain is wrong
        if errs > 0:
            for item in doc_root.find('errors'):
                print(item.text)
            raise SystemExit()

        print('DDNS Record updated successfully!')
        print('%s -> %s' % (self.domain, socket.gethostbyname(self.domain)))
        
