def predict(self, temp_type):
    if temp_type == 'exported':
        temp = self.temp('exported.class')
        return temp.format(class_name=self.class_name, method_name=self.
            method_name, n_features=self.n_features)
    if temp_type == 'embedded':
        meth = self.create_embedded_meth()
        return self.create_embedded_class(meth)