def upvote(self):
    data = self.get_selected_item()
    if 'likes' not in data:
        self.term.flash()
    elif getattr(data['object'], 'archived'):
        self.term.show_notification('Voting disabled for archived post',
            style='Error')
    elif data['likes']:
        with self.term.loader('Clearing vote'):
            data['object'].clear_vote()
        if not self.term.loader.exception:
            data['likes'] = None
    else:
        with self.term.loader('Voting'):
            data['object'].upvote()
        if not self.term.loader.exception:
            data['likes'] = True