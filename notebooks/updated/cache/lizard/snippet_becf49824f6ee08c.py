def publish(self, metrics, config):
    if len(metrics) > 0:
        with open(config['file'], 'a') as outfile:
            for metric in metrics:
                outfile.write(json_format.MessageToJson(metric._pb,
                    including_default_value_fields=True))