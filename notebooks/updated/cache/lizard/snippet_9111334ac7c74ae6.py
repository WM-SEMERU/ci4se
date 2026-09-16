def first(self):
    page = self.get_page(num_elements=1)
    data = self.extract_data(page)
    if data:
        return data[0]