def train_async(train_dataset, eval_dataset, analysis_dir, output_dir,
    features, model_type, max_steps=5000, num_epochs=None, train_batch_size
    =100, eval_batch_size=16, min_eval_frequency=100, top_n=None,
    layer_sizes=None, learning_rate=0.01, epsilon=0.0005, job_name=None,
    job_name_prefix='', cloud=None):
    import google.datalab.utils as du
    if model_type not in ['linear_classification', 'linear_regression',
        'dnn_classification', 'dnn_regression']:
        raise ValueError('Unknown model_type %s' % model_type)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        if cloud:
            return cloud_train(train_dataset=train_dataset, eval_dataset=
                eval_dataset, analysis_dir=analysis_dir, output_dir=
                output_dir, features=features, model_type=model_type,
                max_steps=max_steps, num_epochs=num_epochs,
                train_batch_size=train_batch_size, eval_batch_size=
                eval_batch_size, min_eval_frequency=min_eval_frequency,
                top_n=top_n, layer_sizes=layer_sizes, learning_rate=
                learning_rate, epsilon=epsilon, job_name=job_name,
                job_name_prefix=job_name_prefix, config=cloud)
        else:

            def fn():
                return local_train(train_dataset=train_dataset,
                    eval_dataset=eval_dataset, analysis_dir=analysis_dir,
                    output_dir=output_dir, features=features, model_type=
                    model_type, max_steps=max_steps, num_epochs=num_epochs,
                    train_batch_size=train_batch_size, eval_batch_size=
                    eval_batch_size, min_eval_frequency=min_eval_frequency,
                    top_n=top_n, layer_sizes=layer_sizes, learning_rate=
                    learning_rate, epsilon=epsilon)
            return du.LambdaJob(fn, job_id=None)