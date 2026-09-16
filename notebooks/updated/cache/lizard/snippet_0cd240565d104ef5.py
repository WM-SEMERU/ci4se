def validate(self):
    from .files import HTMLZipFile
    try:
        assert self.kind == content_kinds.HTML5, 'Assumption Failed: Node should be an HTML5 app'
        assert self.questions == [
            ], 'Assumption Failed: HTML should not have questions'
        assert any(filter(lambda f: isinstance(f, HTMLZipFile), self.files)
            ), 'Assumption Failed: HTML should have at least one html file'
        return super(HTML5AppNode, self).validate()
    except AssertionError as ae:
        raise InvalidNodeException('Invalid node ({}): {} - {}'.format(ae.
            args[0], self.title, self.__dict__))