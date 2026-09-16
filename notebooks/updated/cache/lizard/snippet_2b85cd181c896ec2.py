def result(self):
    field = re.sub(REGEX_CLEANER, '', self.field)
    try:
        value = float(self.value)
    except TypeError:
        value = '(%s)' % "', '".join(self.value)
    except ValueError:
        value = str(self.value).replace('\\', '\\\\').replace('"', '\\"'
            ).replace("'", "\\'")
        value = "'%s'" % value
    res = '%s %s %s' % (field, self.operator, value)
    if self.conjunction:
        res = '%s %s' % (self.conjunction, res)
    return res