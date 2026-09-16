def text(self):
    if self.m_name == -1 or self.m_event != const.TEXT:
        return ''
    return self.sb[self.m_name]