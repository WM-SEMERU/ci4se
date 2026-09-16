def update_customer(self, customer_id, customer_deets):
    request = self._put('customers/' + str(customer_id), customer_deets)
    return self.responder(request)