def cli():
    import argparse
    parser = argparse.ArgumentParser(description='Send data to graphite')
    parser.add_argument('metric', metavar='metric', type=str, help=
        'name.of.metric')
    parser.add_argument('value', metavar='value', type=int, help=
        'value of metric as int')
    args = parser.parse_args()
    metric = args.metric
    value = args.value
    graphitesend_instance = init()
    graphitesend_instance.send(metric, value)