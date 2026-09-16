def train_eval():
    global trainloader
    global testloader
    global net
    x_train, y_train = trainloader
    x_test, y_test = testloader
    net.fit(x=x_train, y=y_train, batch_size=args.batch_size,
        validation_data=(x_test, y_test), epochs=args.epochs, shuffle=True,
        callbacks=[SendMetrics(), EarlyStopping(min_delta=0.001, patience=
        10), TensorBoard(log_dir=TENSORBOARD_DIR)])
    _, acc = net.evaluate(x_test, y_test)
    logger.debug('Final result is: %.3f', acc)
    nni.report_final_result(acc)