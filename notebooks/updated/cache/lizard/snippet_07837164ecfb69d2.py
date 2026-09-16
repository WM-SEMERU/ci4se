def monthlyValues(self):
    monthly_values = []
    for value in self.et.find('monthlyValues').findall('value'):
        monthly_values.append(float(value.text))
    return monthly_values