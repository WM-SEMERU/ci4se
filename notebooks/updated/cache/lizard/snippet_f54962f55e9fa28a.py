def generate_template(self, channeldir, filename, header):
    file_path = get_metadata_file_path(channeldir, filename)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as csv_file:
            csvwriter = csv.DictWriter(csv_file, header)
            csvwriter.writeheader()