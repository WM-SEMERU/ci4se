def _mq_callback(self, message):
    try:
        self.logger.info('JobStatusListener {')
        mq_request = MqTransmission.from_json(message.body)
        job_record = self.job_dao.get_by_id(mq_request.process_name,
            mq_request.record_db_id)
        tree_obj = self.timetable.get_tree(job_record.process_name)
        tree_node = tree_obj.get_node(job_record.process_name, job_record.
            timeperiod)
        dependant_nodes = self.timetable._find_dependant_tree_nodes(tree_node)
        handlers_to_trigger = set()
        for node in dependant_nodes:
            state_machine = self.scheduler.state_machine_for(node.process_name)
            if state_machine.run_on_active_timeperiod:
                continue
            handlers_to_trigger.add(self.scheduler.managed_handlers[node.
                process_name])
        for handler in handlers_to_trigger:
            assert isinstance(handler, ManagedThreadHandler)
            handler.trigger()
    except KeyError:
        self.logger.error('Access error for {0}'.format(message.body),
            exc_info=True)
    except Exception:
        self.logger.error('Error during ManagedThreadHandler.trigger call {0}'
            .format(message.body), exc_info=True)
    finally:
        self.consumer.acknowledge(message.delivery_tag)
        self.logger.info('JobStatusListener }')