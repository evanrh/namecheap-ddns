from cli import cli_view, cli_controller

view = cli_view.CLI_View()
c = cli_controller.CLI_Controller(view)
c.main()
