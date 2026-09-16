def split(self, max_commands):
    a_prior = Action(**self.frame)
    a_prior.commands = list(self.commands)
    self.split_actions = [a_prior]
    while len(a_prior.commands) > max_commands:
        a_next = Action(**self.frame)
        a_prior.commands, a_next.commands = a_prior.commands[0:max_commands
            ], a_prior.commands[max_commands:]
        self.split_actions.append(a_next)
        a_prior = a_next
    return self.split_actions