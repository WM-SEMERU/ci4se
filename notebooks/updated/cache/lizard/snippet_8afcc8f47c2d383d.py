def parse_args():
    parser = argparse.ArgumentParser(description=
        'Text Classification with FastText', formatter_class=argparse.
        ArgumentDefaultsHelpFormatter)
    group = parser.add_argument_group('Computation arguments')
    group.add_argument('--input', type=str, help='Input file location')
    group.add_argument('--validation', type=str, help=
        'Validation file Location ')
    group.add_argument('--output', type=str, help=
        'Location to save trained model')
    group.add_argument('--ngrams', type=int, default=1, help=
        'NGrams used for training')
    group.add_argument('--batch_size', type=int, default=16, help=
        'Batch size for training.')
    group.add_argument('--epochs', type=int, default=10, help='Epoch limit')
    group.add_argument('--gpu', type=int, help=
        'Number (index) of GPU to run on, e.g. 0. If not specified, uses CPU.')
    group.add_argument('--no-hybridize', action='store_true', help=
        'Disable hybridization of gluon HybridBlocks.')
    group = parser.add_argument_group('Model arguments')
    group.add_argument('--emsize', type=int, default=100, help=
        'Size of embedding vectors.')
    group = parser.add_argument_group('Optimization arguments')
    group.add_argument('--optimizer', type=str, default='adam')
    group.add_argument('--lr', type=float, default=0.05)
    args = parser.parse_args()
    return args