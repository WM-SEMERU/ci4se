def f1_score(self):
    m_pre = self.precision()
    rec = self.recall()
    return divide(2.0, 1.0 / m_pre + 1.0 / rec)