import requests_client, argparse

class Driver():
    '''
        Basic object to handle creation of the client session
    '''

    def __init__(self):
        self.client = requests_client.Requests_Client()

    def start(self):
        self.client.run()


d = Driver()
d.start()
