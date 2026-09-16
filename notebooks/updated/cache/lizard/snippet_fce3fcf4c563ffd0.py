def envelope(self, header, body):
    env = Element('Envelope', ns=envns)
    env.addPrefix(Namespace.xsins[0], Namespace.xsins[1])
    env.append(header)
    env.append(body)
    return env