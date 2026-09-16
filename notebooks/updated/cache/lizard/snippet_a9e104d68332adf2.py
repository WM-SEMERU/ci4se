def preloop(self):
    if not self.already_prelooped:
        self.already_prelooped = True
        open('.psiturk_history', 'a').close()
        readline.read_history_file('.psiturk_history')
        for i in range(readline.get_current_history_length()):
            if readline.get_history_item(i) is not None:
                self.history.append(readline.get_history_item(i))