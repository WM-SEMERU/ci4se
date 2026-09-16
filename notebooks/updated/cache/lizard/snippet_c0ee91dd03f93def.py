def get_all_subcommands(self):
    subcommands = []
    for command in self.descrip:
        for word in command.split():
            for kid in self.command_tree.children:
                if word != kid and word not in subcommands:
                    subcommands.append(word)
    return subcommands