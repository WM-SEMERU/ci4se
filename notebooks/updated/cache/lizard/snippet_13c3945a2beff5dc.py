def predict(self, text):
    pred = self.predict_proba(text)
    tags = self._get_tags(pred)
    return tags