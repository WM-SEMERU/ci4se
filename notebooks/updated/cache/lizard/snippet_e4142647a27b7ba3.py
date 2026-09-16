def execute_plan(self, plan, allow_rf_change=False):
    if self.should_execute():
        result = self.zk.execute_plan(plan, allow_rf_change=allow_rf_change)
        if not result:
            self.log.error('Plan execution unsuccessful.')
            sys.exit(1)
        else:
            self.log.info(
                'Plan sent to zookeeper for reassignment successfully.')
    else:
        self.log.info(
            "Proposed plan won't be executed (--apply and confirmation needed)."
            )