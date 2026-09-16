def generate_parameters(self, parameter_id):
    if not self.history:
        self.init_search()
    new_father_id = None
    generated_graph = None
    if not self.training_queue:
        new_father_id, generated_graph = self.generate()
        new_model_id = self.model_count
        self.model_count += 1
        self.training_queue.append((generated_graph, new_father_id,
            new_model_id))
        self.descriptors.append(generated_graph.extract_descriptor())
    graph, father_id, model_id = self.training_queue.pop(0)
    json_model_path = os.path.join(self.path, str(model_id) + '.json')
    json_out = graph_to_json(graph, json_model_path)
    self.total_data[parameter_id] = json_out, father_id, model_id
    return json_out