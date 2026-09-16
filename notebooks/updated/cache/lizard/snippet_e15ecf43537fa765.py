def partition_dataset():
    dataset = datasets.MNIST('./data', train=True, download=True, transform
        =transforms.Compose([transforms.ToTensor(), transforms.Normalize((
        0.1307,), (0.3081,))]))
    size = dist.get_world_size()
    bsz = 128 / float(size)
    partition_sizes = [(1.0 / size) for _ in range(size)]
    partition = DataPartitioner(dataset, partition_sizes)
    partition = partition.use(dist.get_rank())
    train_set = torch.utils.data.DataLoader(partition, batch_size=int(bsz),
        shuffle=True)
    return train_set, bsz