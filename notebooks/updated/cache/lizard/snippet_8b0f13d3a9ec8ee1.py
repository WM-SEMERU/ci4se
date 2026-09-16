def _PrintEventsStatus(self, events_status):
    if events_status:
        table_view = views.CLITabularTableView(column_names=['Events:',
            'Filtered', 'In time slice', 'Duplicates', 'MACB grouped',
            'Total'], column_sizes=[15, 15, 15, 15, 15, 0])
        table_view.AddRow(['', events_status.number_of_filtered_events,
            events_status.number_of_events_from_time_slice, events_status.
            number_of_duplicate_events, events_status.
            number_of_macb_grouped_events, events_status.
            total_number_of_events])
        self._output_writer.Write('\n')
        table_view.Write(self._output_writer)