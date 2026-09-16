def json(self):
    insndescs = [{insndesc['instruction']: insndesc['value']} for insndesc in
        self.structure]
    return json.dumps(insndescs)