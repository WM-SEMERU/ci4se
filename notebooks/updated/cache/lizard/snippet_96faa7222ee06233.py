def setup_regex(self):
    self._RX_CONTAINS = '^\\s*contains[^\\n]*?$'
    self.RE_CONTAINS = re.compile(self._RX_CONTAINS, re.M | re.I)
    self._RX_EXEC = (
        '\\n[ \\t]*((?P<type>character|real|type|logical|integer|complex)?' +
        '(?P<kind>\\([a-z0-9_]+\\))?)?((?P<modifiers>[\\w, \\t]+?))?[ \\t]*' +
        '(?P<codetype>subroutine|function)\\s+(?P<name>[^(]+)' +
        '\\s*\\((?P<parameters>[^)]*)\\)(?P<result>\\sresult\\([a-z0-9_]+\\))?'
         + '(?P<contents>.+?)end\\s*(?P=codetype)\\s+(?P=name)')
    self.RE_EXEC = re.compile(self._RX_EXEC, re.DOTALL | re.I)
    self._RX_SIG = (
        '((?P<type>character|real|type|logical|integer|complex)?' +
        '(?P<kind>\\([a-z0-9_]+\\))?)?(,?(?P<modifiers>[^\\n]+?))?\\s*' +
        '(?P<codetype>subroutine|function)\\s+(?P<name>[^(]+)' +
        '\\s*\\((?P<parameters>[^)]*)\\)')
    self.RE_SIG = re.compile(self._RX_SIG, re.I)
    self._RX_ASSIGN = '^(?P<assignee>[^!<=\\n/]+?)=[^\\n]+?$'
    self.RE_ASSIGN = re.compile(self._RX_ASSIGN, re.M)
    self._RX_DEPEND = (
        '^\\s*(?P<sub>call\\s+)?(?P<exec>[a-z0-9_%]+\\s*\\([^\\n]+)$')
    self.RE_DEPEND = re.compile(self._RX_DEPEND, re.M | re.I)
    self._RX_DEPCLEAN = '(?P<key>[a-z0-9_%]+)\\('
    self.RE_DEPCLEAN = re.compile(self._RX_DEPCLEAN, re.I)
    self._RX_CONST = '[^"\']+(?P<const>["\'][^\'"]+["\'])'
    self.RE_CONST = re.compile(self._RX_CONST)
    self._RX_COMMENTS = '\\s*![^\\n"]+?\\n'
    self.RE_COMMENTS = re.compile(self._RX_COMMENTS)