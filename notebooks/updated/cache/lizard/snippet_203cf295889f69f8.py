def _delete_example(self, request):
    index = int(request.args.get('index'))
    if index >= len(self.examples):
        return http_util.Respond(request, {'error':
            'invalid index provided'}, 'application/json', code=400)
    del self.examples[index]
    self.updated_example_indices = set([(i if i < index else i - 1) for i in
        self.updated_example_indices])
    self.generate_sprite([ex.SerializeToString() for ex in self.examples])
    return http_util.Respond(request, {}, 'application/json')