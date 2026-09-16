def widget_df(self):
    if hasattr(self, 'widget_instance') == True:
        if self.widget_instance.mat_string != '':
            tmp_net = deepcopy(Network())
            df_string = self.widget_instance.mat_string
            tmp_net.load_file_as_string(df_string)
            df = tmp_net.export_df()
            return df
        else:
            return self.export_df()
    elif hasattr(self, 'widget_class') == True:
        print('Please make the widget before exporting the widget DataFrame.')
        print('Do this using the widget method: net.widget()')
    else:
        print(
            'Can not make widget because Network has no attribute widget_class'
            )
        print(
            'Please instantiate Network with clustergrammer_widget using: Network(clustergrammer_widget)'
            )