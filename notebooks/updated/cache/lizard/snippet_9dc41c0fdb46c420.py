def parse_code(self):
    code = open(self.path, encoding='utf-8').read()
    try:
        body = ast.parse(code).body
    except SyntaxError:
        try:
            code = code.encode('utf-8')
            body = ast.parse(code).body
        except SyntaxError:
            return []
    return self.get_imports(body)