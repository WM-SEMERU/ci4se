def get_number_of_particles():
    with open('dynac.short') as f:
        data_str = ''.join(line for line in f.readlines())
        num_of_parts = int(data_str.split('Simulation with')[1].strip().
            split()[0])
    return num_of_parts