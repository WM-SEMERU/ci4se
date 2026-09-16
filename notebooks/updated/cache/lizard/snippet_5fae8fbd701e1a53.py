def sec_com_channels(self):
    metrics = self.config['com_channels']['activity_metrics']
    metrics += self.config['com_channels']['author_metrics']
    for metric in metrics:
        csv_labels = 'labels,' + metric.id
        file_label = metric.ds.name + '_' + metric.id
        title_label = metric.name + ' per ' + self.interval
        self.__create_csv_eps(metric, None, csv_labels, file_label, title_label
            )