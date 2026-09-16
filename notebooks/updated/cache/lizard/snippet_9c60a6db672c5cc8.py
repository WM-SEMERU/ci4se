def is_tensor_final(self, tensor_name):
    tensor = self._name_to_tensor(tensor_name)
    return tensor in self._final_tensors