def esp(self):
    result = np.zeros(self.numc, float)
    for index1 in range(self.numc):
        result[index1] = self.esp_component(index1)
    return result