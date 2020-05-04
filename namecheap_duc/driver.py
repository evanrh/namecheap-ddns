import client, argparse

'''
    Basic object to handle creation of the client session
'''
class Driver():
    def __init__(self):
        self.client = client.Client()

    def start(self):
        self.client.run()

