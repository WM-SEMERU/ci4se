def format_metric_values(self, metric_values):
    loss_str = 'N/A'
    accuracy_str = 'N/A'
    try:
        loss_str = 'loss: %.3f' % metric_values[0]
        accuracy_str = 'accuracy: %.3f' % metric_values[1]
    except (TypeError, IndexError):
        pass
    return '%s, %s' % (loss_str, accuracy_str)