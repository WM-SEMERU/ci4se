def tt_avg(self, print_output=True, output_file='tt.csv'):
    avg = self.tt.mean(axis=2)
    if print_output:
        np.savetxt(output_file, avg, delimiter=',')
    return avg