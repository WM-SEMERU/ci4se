def onecmd(self, line):
    try:
        return cmd.Cmd.onecmd(self, line)
    except Exception as e:
        print('Critical error.', e)