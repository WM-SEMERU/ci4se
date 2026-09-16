def update_shipment(self, resource_id, data):
    return Shipments(self.client).on(self).update(resource_id, data)