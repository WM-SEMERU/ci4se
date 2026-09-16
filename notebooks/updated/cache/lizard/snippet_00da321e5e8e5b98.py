def _setup_metric_group_values(self):
    mg_defs = self._metrics_context.metric_group_definitions
    metric_group_name = None
    resource_uri = None
    dt_timestamp = None
    object_values = None
    metric_group_values = list()
    state = 0
    for mr_line in self._metrics_response_str.splitlines():
        if state == 0:
            if object_values is not None:
                mgv = MetricGroupValues(metric_group_name, object_values)
                metric_group_values.append(mgv)
                object_values = None
            if mr_line == '':
                pass
            else:
                metric_group_name = mr_line.strip('"')
                assert metric_group_name in mg_defs
                m_defs = mg_defs[metric_group_name].metric_definitions
                object_values = list()
                state = 1
        elif state == 1:
            if mr_line == '':
                state = 0
            else:
                resource_uri = mr_line.strip('"')
                state = 2
        elif state == 2:
            assert mr_line != ''
            try:
                dt_timestamp = datetime_from_timestamp(int(mr_line))
            except ValueError:
                dt_timestamp = datetime.now(pytz.utc)
            state = 3
        elif state == 3:
            if mr_line != '':
                str_values = mr_line.split(',')
                metrics = dict()
                for m_name in m_defs:
                    m_def = m_defs[m_name]
                    m_type = m_def.type
                    m_value_str = str_values[m_def.index]
                    m_value = _metric_value(m_value_str, m_type)
                    metrics[m_name] = m_value
                ov = MetricObjectValues(self._client, mg_defs[
                    metric_group_name], resource_uri, dt_timestamp, metrics)
                object_values.append(ov)
            else:
                state = 1
    return metric_group_values