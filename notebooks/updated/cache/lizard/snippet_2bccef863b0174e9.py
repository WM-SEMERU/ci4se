def to_dict(self):
    return {'prediction': self.prediction_file.to_dict(), 'attachments': [a
        .to_dict() for a in self.attachments]}