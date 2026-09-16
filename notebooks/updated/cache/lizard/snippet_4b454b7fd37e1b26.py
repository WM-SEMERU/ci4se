def benchmark(cores, args):
    model = args.module
    fileInput = args.input_file
    fileOutput = args.output_file
    batchsize = args.batch_size
    thread = []
    for i in range(cores):
        command = (
            'taskset -c %d-%d python3 -m sockeye.translate -m %s -i %s -o %s --batch-size %d --output-type benchmark --use-cpu > /dev/null 2>&1 '
             % (i, i, model, fileInput, fileOutput, batchsize))
        t = threading.Thread(target=task, args=(command,))
        thread.append(t)
        t.start()
    for t in thread:
        t.join()