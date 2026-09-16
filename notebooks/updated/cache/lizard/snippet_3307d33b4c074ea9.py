def build_intent(self, intent_name):
    is_fallback = self.assist._intent_fallbacks[intent_name]
    contexts = self.assist._required_contexts[intent_name]
    events = self.assist._intent_events[intent_name]
    new_intent = Intent(intent_name, fallback_intent=is_fallback, contexts=
        contexts, events=events)
    self.build_action(new_intent)
    self.build_user_says(new_intent)
    return new_intent