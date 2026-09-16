def delete_message(self, message, callback=None):
    return self.connection.delete_message(self, message, callback=callback)