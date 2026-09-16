def get_operator_output_port(self):
    return OperatorOutputPort(self.rest_client.make_request(self.
        operatorOutputPort), self.rest_client)