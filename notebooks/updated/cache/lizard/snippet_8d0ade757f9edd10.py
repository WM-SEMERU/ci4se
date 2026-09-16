def assert_union(self, collection1, collection2, failure_message=
    'Expected overlap between collections: "{}" and "{}"'):
    assertion = lambda : len(collection1 or collection2) > 0
    failure_message = unicode(failure_message).format(collection1, collection2)
    self.webdriver_assert(assertion, failure_message)