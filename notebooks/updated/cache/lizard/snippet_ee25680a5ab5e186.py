def save(self):
    if self.save_option == 'curdir':
        model_path = os.path.join(os.getcwd(), '{}.lcopt'.format(self.name))
    else:
        model_path = os.path.join(storage.model_dir, '{}.lcopt'.format(self
            .name))
    model_path = fix_mac_path_escapes(model_path)
    with open(model_path, 'wb') as model_file:
        pickle.dump(self, model_file)