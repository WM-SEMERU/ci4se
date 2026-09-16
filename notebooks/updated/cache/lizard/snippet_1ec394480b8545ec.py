def write_file(self):
    try:
        with open(self.experiment_file, 'w') as file:
            json.dump(self.experiments, file)
    except IOError as error:
        print('Error:', error)
        return