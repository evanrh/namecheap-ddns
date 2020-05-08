
import sys
from . import cli_view

sys.path.append('../')
import no_reqs_client

class CLI_Controller():

    def __init__(self, view=None):
        self.view = view

    # Just in case it isn't passed in the constructor
    def register_view(self, view):
        self.view = view

    # Main logic of controller
    def main(self):

        # Get cli args to be used in program
        args = vars(self.view.parse_args())

        # Required options not supplied by user
        while args['domain'] == '' or args['domain'] == None:
            args['domain'] = self.view.get_domain()

        while args['pass'] == '' or args['pass'] == None:
            args['pass'] = self.view.get_password()

        # Create client from passed in args
        self.model = no_reqs_client.No_Reqs_Client(host=args['host'],
                    domain=args['domain'], passwd=args['pass'], ip_addr = args['address'])

        result = self.model.run()

        # Error(s) updating record
        if not result:
            for err in self.model.get_errs():
                self.view.print_string(err.text)
            raise SystemExit()

        # Successful update of record
        self.view.print_string('DDNS record for {} updated!'.format(args['domain']))
        self.view.print_string('{} -> {}'.format(args['domain'], self.model.get_ip()))
