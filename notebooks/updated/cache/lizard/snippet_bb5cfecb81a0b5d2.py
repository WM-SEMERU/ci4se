def do_mirror(self, params):
    question = 'Are you sure you want to replace %s with %s?' % (params.dst,
        params.src)
    if params.skip_prompt or self.prompt_yes_no(question):
        self.copy(params, True, True, 0, True)