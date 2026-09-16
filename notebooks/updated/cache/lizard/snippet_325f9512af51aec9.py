def _create_log_entry(self, log_record_pyxb):
    event_log_model = d1_gmn.app.event_log.create_log_entry(d1_gmn.app.
        model_util.get_sci_model(d1_common.xml.get_req_val(log_record_pyxb.
        identifier)), log_record_pyxb.event, log_record_pyxb.ipAddress,
        log_record_pyxb.userAgent, log_record_pyxb.subject.value())
    event_log_model.timestamp = d1_common.date_time.normalize_datetime_to_utc(
        log_record_pyxb.dateLogged)
    event_log_model.save()