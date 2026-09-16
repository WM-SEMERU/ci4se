def eval_policy(eval_positions):
    model_paths = oneoff_utils.get_model_paths(fsdb.models_dir())
    idx_start = FLAGS.idx_start
    eval_every = FLAGS.eval_every
    print('Evaluating models {}-{}, eval_every={}'.format(idx_start, len(
        model_paths), eval_every))
    player = None
    for i, idx in enumerate(tqdm(range(idx_start, len(model_paths),
        eval_every))):
        if player and i % 20 == 0:
            player.network.sess.close()
            tf.reset_default_graph()
            player = None
        if not player:
            player = oneoff_utils.load_player(model_paths[idx])
        else:
            oneoff_utils.restore_params(model_paths[idx], player)
        pos_names, positions = zip(*eval_positions)
        eval_probs, eval_values = player.network.run_many(positions)
        for pos_name, probs, value in zip(pos_names, eval_probs, eval_values):
            save_file = os.path.join(FLAGS.data_dir, 'heatmap-{}-{}.csv'.
                format(pos_name, idx))
            with open(save_file, 'w') as data:
                data.write('{},  {},  {}\n'.format(idx, value, ','.join(map
                    (str, probs))))