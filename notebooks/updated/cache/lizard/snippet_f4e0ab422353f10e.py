def replace(self):
    doc_dict = self.doc_dict.copy()
    for k, v in doc_dict.items():
        if '{' and '}' in v:
            self.doc_dict[k] = v.format(**doc_dict)