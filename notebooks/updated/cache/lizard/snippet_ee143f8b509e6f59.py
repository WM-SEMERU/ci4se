def on_pbnBack_released(self):
    current_step = self.get_current_step()
    if current_step.step_type == STEP_FC:
        new_step = self.impact_function_steps.pop()
    elif current_step.step_type == STEP_KW:
        try:
            new_step = self.keyword_steps.pop()
        except IndexError:
            new_step = self.impact_function_steps.pop()
    else:
        raise InvalidWizardStep
    if new_step == self.step_fc_functions1:
        self.step_fc_functions1.tblFunctions1.setFocus()
    if new_step == self.step_fc_functions2:
        self.step_fc_functions2.tblFunctions2.setFocus()
    if new_step == self.step_fc_extent:
        self.step_fc_extent.set_widgets()
    self.pbnNext.setText(tr('Next'))
    self.pbnNext.setEnabled(True)
    self.go_to_step(new_step)