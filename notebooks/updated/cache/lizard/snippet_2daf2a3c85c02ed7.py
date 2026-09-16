def subscriber_choice_control(self):
    self.current.task_data['option'] = None
    self.current.task_data['chosen_subscribers'
        ], names = self.return_selected_form_items(self.input['form'][
        'SubscriberList'])
    self.current.task_data['msg'
        ] = 'You should choose at least one subscriber for migration operation.'
    if self.current.task_data['chosen_subscribers']:
        self.current.task_data['option'] = self.input['cmd']
        del self.current.task_data['msg']