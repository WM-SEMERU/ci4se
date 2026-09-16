def load_dataloader(self):
    input_transform = transforms.Compose([transforms.ToTensor(), transforms
        .Normalize((0.7136, 0.4906, 0.3283), (0.1138, 0.1078, 0.0917))])
    training_dataset = LipsDataset(self.image_path, self.align_path, mode=
        'train', transform=input_transform, seq_len=self.seq_len)
    self.train_dataloader = mx.gluon.data.DataLoader(training_dataset,
        batch_size=self.batch_size, shuffle=True, num_workers=self.num_workers)
    valid_dataset = LipsDataset(self.image_path, self.align_path, mode=
        'valid', transform=input_transform, seq_len=self.seq_len)
    self.valid_dataloader = mx.gluon.data.DataLoader(valid_dataset,
        batch_size=self.batch_size, shuffle=True, num_workers=self.num_workers)