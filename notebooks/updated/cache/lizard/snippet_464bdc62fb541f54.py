def train(epoch):
    global trainloader
    global testloader
    global net
    global criterion
    global optimizer
    logger.debug('Epoch: %d', epoch)
    net.train()
    train_loss = 0
    correct = 0
    total = 0
    for batch_idx, (inputs, targets) in enumerate(trainloader):
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()
        acc = 100.0 * correct / total
        logger.debug('Loss: %.3f | Acc: %.3f%% (%d/%d)', train_loss / (
            batch_idx + 1), 100.0 * correct / total, correct, total)
    return acc