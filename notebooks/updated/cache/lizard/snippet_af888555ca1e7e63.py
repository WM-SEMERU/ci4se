def run(params):
    rank = dist.get_rank()
    torch.manual_seed(1234)
    train_set, bsz = partition_dataset()
    model = Net()
    model = model
    optimizer = optim.SGD(model.parameters(), lr=params['learning_rate'],
        momentum=params['momentum'])
    num_batches = ceil(len(train_set.dataset) / float(bsz))
    total_loss = 0.0
    for epoch in range(3):
        epoch_loss = 0.0
        for data, target in train_set:
            data, target = Variable(data), Variable(target)
            optimizer.zero_grad()
            output = model(data)
            loss = F.nll_loss(output, target)
            epoch_loss += loss.item()
            loss.backward()
            average_gradients(model)
            optimizer.step()
        if rank == 0:
            nni.report_intermediate_result(epoch_loss / num_batches)
        total_loss += epoch_loss / num_batches
    total_loss /= 3
    logger.debug('Final loss: {}'.format(total_loss))
    if rank == 0:
        nni.report_final_result(total_loss)