def createDenseCNNModel(self):
    model = nn.Sequential(nn.Conv2d(in_channels=self.in_channels,
        out_channels=self.out_channels[0], kernel_size=self.kernel_size[0],
        stride=self.stride[0], padding=self.padding[0]), nn.MaxPool2d(
        kernel_size=2), nn.ReLU(), nn.Conv2d(in_channels=self.out_channels[
        0], out_channels=self.out_channels[1], kernel_size=self.kernel_size
        [1], stride=self.stride[1], padding=self.padding[1]), nn.MaxPool2d(
        kernel_size=2), nn.ReLU(), Flatten(), nn.Linear(self.cnn_output_len
        [1], self.n), nn.ReLU(), nn.Linear(self.n, self.output_size), nn.
        LogSoftmax(dim=1))
    model.to(self.device)
    if torch.cuda.device_count() > 1:
        model = torch.nn.DataParallel(model)
    return model