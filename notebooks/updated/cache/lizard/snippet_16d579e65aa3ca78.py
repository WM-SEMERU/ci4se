def execute_before_scenario_steps(self, context):
    if not self.feature_error:
        self.__execute_steps_by_action(context, ACTIONS_BEFORE_SCENARIO)
    if context.dyn_env.scenario_error:
        context.scenario.mark_skipped()