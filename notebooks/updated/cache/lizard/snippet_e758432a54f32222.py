def load_data_subject_areas(subject_file):
    lst = []
    if os.path.exists(subject_file):
        with open(subject_file, 'r') as f:
            for line in f:
                lst.append(line.strip())
    else:
        print('MISSING DATA FILE (subject_file) ', subject_file)
        print('update your config.py or config.txt')
    return lst