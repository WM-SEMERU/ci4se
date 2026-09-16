def forward(self, x):
    head_outputs = [None] * self.t
    if isinstance(self.input_layer, list):
        input_outputs = [mod(x) for mod, x in zip(self.input_layer, x)]
        x = torch.stack(input_outputs, dim=1)
        for t in self.task_map[0]:
            head = self.heads[t]
            head_outputs[t] = head(input_outputs[t])
    else:
        x = self.input_layer(x)
        for t in self.task_map[0]:
            head = self.heads[t]
            head_outputs[t] = head(x)
    for i, layer in enumerate(self.middle_layers, start=1):
        x = layer(x)
        for t in self.task_map[i]:
            head = self.heads[t]
            if self.config['pass_predictions'] and bool(self.task_graph.
                parents[t]):
                task_input = [x]
                for p in self.task_graph.parents[t]:
                    task_input.append(head_outputs[p])
                task_input = torch.stack(task_input, dim=1)
            else:
                task_input = x
            head_outputs[t] = head(task_input)
    return head_outputs