def verify_valid_dependencies(self):
    unobserved_dependencies = set(self.tasks.keys())
    target_queue = []
    while len(unobserved_dependencies) > 0:
        target_queue = [unobserved_dependencies.pop()]
        while target_queue is not []:
            target_queue += unobserved_dependencies