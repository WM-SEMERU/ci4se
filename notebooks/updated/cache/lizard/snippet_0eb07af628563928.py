def train(train_dataset, eval_dataset, analysis_dir, output_dir, features,
    layer_sizes, max_steps=5000, num_epochs=None, train_batch_size=100,
    eval_batch_size=16, min_eval_frequency=100, learning_rate=0.01, epsilon
    =0.0005, job_name=None, cloud=None):
    job = train_async(train_dataset=train_dataset, eval_dataset=
        eval_dataset, analysis_dir=analysis_dir, output_dir=output_dir,
        features=features, layer_sizes=layer_sizes, max_steps=max_steps,
        num_epochs=num_epochs, train_batch_size=train_batch_size,
        eval_batch_size=eval_batch_size, min_eval_frequency=
        min_eval_frequency, learning_rate=learning_rate, epsilon=epsilon,
        job_name=job_name, cloud=cloud)
    job.wait()
    print('Training: ' + str(job.state))