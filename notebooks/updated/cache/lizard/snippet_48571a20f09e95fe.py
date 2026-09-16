def evaluate():
    print(eval_model)
    eval_model.initialize(mx.init.Xavier(), ctx=context[0])
    eval_model.hybridize(static_alloc=True, static_shape=True)
    epoch = args.from_epoch if args.from_epoch else 0
    while epoch < args.epochs:
        checkpoint_name = '%s.%s' % (args.save, format(epoch, '02d'))
        if not os.path.exists(checkpoint_name):
            print('Wait for a new checkpoint...')
            time.sleep(600)
            continue
        eval_model.load_parameters(checkpoint_name)
        print('Loaded parameters from checkpoint %s' % checkpoint_name)
        start_epoch_time = time.time()
        final_test_L = test(test_data, test_batch_size, ctx=context[0])
        end_epoch_time = time.time()
        print('[Epoch %d] test loss %.2f, test ppl %.2f' % (epoch,
            final_test_L, math.exp(final_test_L)))
        print('Epoch %d took %.2f seconds.' % (epoch, end_epoch_time -
            start_epoch_time))
        sys.stdout.flush()
        epoch += 1