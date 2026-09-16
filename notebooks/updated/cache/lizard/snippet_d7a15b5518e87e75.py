def create_dag(self, dependencies):
    dag = DirectedGraph()
    for dep in dependencies:
        for vertex in dep.inputs:
            task_uuid = vertex.private_task_config.uuid
            if task_uuid not in self.uuid_dict:
                raise ValueError(
                    'Task {}, which is an input of a task {}, is not part of the defined workflow'
                    .format(vertex.__class__.__name__, dep.name))
            dag.add_edge(self.uuid_dict[task_uuid], dep)
        if not dep.inputs:
            dag.add_vertex(dep)
    return dag