def decimal(self, prompt, default=None, lower=None, upper=None):
    prompt = prompt if prompt is not None else 'Enter a decimal number'
    prompt += ' [{0}]: '.format(default) if default is not None else ': '
    return self.input(curry(filter_decimal, default=default, lower=lower,
        upper=upper), prompt)