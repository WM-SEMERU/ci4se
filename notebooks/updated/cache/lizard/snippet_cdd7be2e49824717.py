def delete_all_product_sets(self):
    api_url = super(ProductSetAPI, self).base_url
    return self.client.delete(api_url)