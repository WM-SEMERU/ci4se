def p_ansible_sentence(self, t):
    t[0] = ansible(t[2], t[4], line=t.lineno(1))