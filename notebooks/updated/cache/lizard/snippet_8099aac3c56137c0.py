def imshow(self, key):
    data = self.model.get_data()
    import spyder.pyplot as plt
    plt.figure()
    plt.imshow(data[key])
    plt.show()