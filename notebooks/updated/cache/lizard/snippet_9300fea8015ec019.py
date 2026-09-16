def make_back_matter(self):
    body = self.main.getroot().find('body')
    if self.article.root.find('back') is None:
        return
    back_ack = self.make_back_acknowledgments()
    if back_ack is not None:
        body.append(back_ack)
    self.make_back_author_contributions(body)
    self.make_back_glossary(body)
    self.make_back_notes(body)