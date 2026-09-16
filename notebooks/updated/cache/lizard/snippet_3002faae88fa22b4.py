def delete_stack(self, stack_name):
    get_stack(stack_name)
    CLIENT.delete_stack(StackName=stack_name)
    DELETE_WAITER.wait(StackName=stack_name)