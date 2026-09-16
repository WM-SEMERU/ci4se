def ends_with(self, other):

    @Parser
    def ends_with_parser(text, index):
        res = self(text, index)
        if not res.status:
            return res
        end = other(text, res.index)
        if end.status:
            return res
        else:
            return Value.failure(end.index, 'ends with {}'.format(end.expected)
                )
    return ends_with_parser