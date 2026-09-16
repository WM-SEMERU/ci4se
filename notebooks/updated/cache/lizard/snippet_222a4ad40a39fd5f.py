def set_tensor_final(self, tensor_name):
    tensor = self._name_to_tensor(tensor_name)
    self._final_tensors.add(tensor)