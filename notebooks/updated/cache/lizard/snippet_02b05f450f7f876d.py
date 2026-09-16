def set_prompt(scope, prompt=None):
    conn = scope.get('__connection__')
    conn.set_prompt(prompt)
    return True