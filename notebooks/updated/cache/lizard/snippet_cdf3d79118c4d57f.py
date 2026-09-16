def dbg_exec_magic(self, magic, args=''):
    code = "!get_ipython().kernel.shell.run_line_magic('{}', '{}')".format(
        magic, args)
    self.kernel_client.input(code)