def delete_customer(self, handle):
    self.request(E.deleteCustomerRequest(E.handle(handle)))
    return True