def plot(self, qubit_subset=None):
    import matplotlib.pyplot as plt
    prob_dict = self.get_outcome_probs()
    if qubit_subset:
        sub_dict = {}
        qubit_num = len(self)
        for i in qubit_subset:
            if i > 2 ** qubit_num - 1:
                raise IndexError('Index {} too large for {} qubits.'.format
                    (i, qubit_num))
            else:
                sub_dict[get_bitstring_from_index(i, qubit_num)] = prob_dict[
                    get_bitstring_from_index(i, qubit_num)]
        prob_dict = sub_dict
    plt.bar(range(len(prob_dict)), prob_dict.values(), align='center',
        color='#6CAFB7')
    plt.xticks(range(len(prob_dict)), prob_dict.keys())
    plt.show()