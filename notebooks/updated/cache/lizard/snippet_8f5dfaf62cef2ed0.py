def query(self, selector, context=None):
    element = self.client.create_element('browser.query', (selector, context))
    return DOMNode.factory(element, self)