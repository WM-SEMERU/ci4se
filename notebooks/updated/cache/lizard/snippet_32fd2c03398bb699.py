def check(sensor_class, args):
    parser = SensorCmdLine.parsers(sensor_class)
    parsed = parser.parse_args(args)
    return sensor_class.check(json.loads(parsed.data))