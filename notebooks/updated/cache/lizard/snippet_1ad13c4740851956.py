def device_product_str(self, indent):
    s = 'Vendor: {}\n'.format(self.vendor)
    s += indent + 'Product: {}\n'.format(self.product and product_map[self.
        product] or 'Unknown')
    s += indent + 'Version: {}\n'.format(self.version)
    return s