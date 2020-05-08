
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
        self.err_list = []

    def run(self):
        return self.__update_record()

    def __update_record(self):

        # Define site update params
        params = {'domain': self.domain, 'password': self.passwd}

        if self.host != None:
            params['host'] = self.host
        if self.ip_addr != None:
            params['ip'] = self.ip_addr

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
                self.err_list.append(item)
            return False

        return True

    def get_ip(self):
        return socket.gethostbyname(self.domain)

    def get_errs(self):
        return self.err_list
                
