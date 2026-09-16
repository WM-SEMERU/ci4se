def _mq_callback(self, message):
    try:
        self.logger.info('UowStatusListener {')
        mq_request = MqTransmission.from_json(message.body)
        uow = self.uow_dao.get_one(mq_request.record_db_id)
        if uow.unit_of_work_type != unit_of_work.TYPE_MANAGED:
            self.logger.info(
                'Received transmission from non-managed UOW execution: {0}. Ignoring it.'
                .format(uow.unit_of_work_type))
            return
        tree = self.timetable.get_tree(uow.process_name)
        node = tree.get_node(uow.process_name, uow.timeperiod)
        if uow.db_id != node.job_record.related_unit_of_work:
            self.logger.info(
                'Received transmission is likely outdated. Ignoring it.')
            return
        if not uow.is_finished:
            self.logger.info(
                'Received transmission from {0}@{1} in non-final state {2}. Ignoring it.'
                .format(uow.process_name, uow.timeperiod, uow.state))
            return
        state_machine = self.scheduler.state_machine_for(node.process_name)
        self.logger.info(
            'Commencing StateMachine.notify with UOW from {0}@{1} in {2}.'.
            format(uow.process_name, uow.timeperiod, uow.state))
        state_machine.notify(uow)
    except KeyError:
        self.logger.error('Access error for {0}'.format(message.body),
            exc_info=True)
    except Exception:
        self.logger.error('Error during StateMachine.notify call {0}'.
            format(message.body), exc_info=True)
    finally:
        self.consumer.acknowledge(message.delivery_tag)
        self.logger.info('UowStatusListener }')