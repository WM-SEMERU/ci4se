def retrieve_customer(self, handle, with_additional_data=False):
    response = self.request(E.retrieveCustomerRequest(E.handle(handle), E.
        withAdditionalData(int(with_additional_data))))
    return response.as_model(Customer)