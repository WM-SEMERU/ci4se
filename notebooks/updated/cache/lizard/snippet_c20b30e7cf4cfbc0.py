def addDelay(self, urlPattern='', delay=0, httpMethod=None):
    print('addDelay is deprecated please use delays instead')
    delay = {'urlPattern': urlPattern, 'delay': delay}
    if httpMethod:
        delay['httpMethod'] = httpMethod
    return self.delays(delays={'data': [delay]})