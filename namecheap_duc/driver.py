import client, argparse

class Driver():
    def __init__(self):
        self.client = client.Client()

    def start(self):
        self.client.run()

