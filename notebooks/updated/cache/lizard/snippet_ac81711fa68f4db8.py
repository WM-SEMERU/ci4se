def _handle_backward_execution_after_child_execution(self):
    self.child_state.state_execution_status = (StateExecutionStatus.
        WAIT_FOR_NEXT_STATE)
    last_history_item = self.execution_history.pop_last_item()
    assert isinstance(last_history_item, CallItem)
    self.scoped_data = last_history_item.scoped_data
    last_history_item = self.execution_history.get_last_history_item()
    if last_history_item.state_reference is self:
        last_history_item = self.execution_history.pop_last_item()
        assert isinstance(last_history_item, CallItem)
        self.scoped_data = last_history_item.scoped_data
        self.child_state.state_execution_status = StateExecutionStatus.INACTIVE
        return True
    return False