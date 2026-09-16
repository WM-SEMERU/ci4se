def ExpireRules(self):
    rules = self.Get(self.Schema.RULES)
    new_rules = self.Schema.RULES()
    now = time.time() * 1000000.0
    expired_session_ids = set()
    for rule in rules:
        if rule.expires > now:
            new_rules.Append(rule)
        else:
            for action in rule.actions:
                if action.hunt_id:
                    expired_session_ids.add(action.hunt_id)
    if expired_session_ids:
        with data_store.DB.GetMutationPool() as pool:
            manager = queue_manager.QueueManager(token=self.token)
            manager.MultiNotifyQueue([rdf_flows.GrrNotification(session_id=
                session_id) for session_id in expired_session_ids],
                mutation_pool=pool)
    if len(new_rules) < len(rules):
        self.Set(self.Schema.RULES, new_rules)
        self.Flush()