import requests_client, argparse
import no_reqs_client

class Driver():
    '''
        Basic object to handle creation of the client session
    '''

    def __init__(self):
        self.client = no_reqs_client.No_Reqs_Client()

    def start(self):
        self.client.run()


d = Driver()
d.start()
