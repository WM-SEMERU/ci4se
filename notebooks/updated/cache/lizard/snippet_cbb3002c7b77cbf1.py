def choice(self, subscribers, message):
    if not subscribers:
        return None
    reliable_subscribers = [s for s in subscribers if s.reliable_subscriber]
    if reliable_subscribers:
        return random.choice(reliable_subscribers)
    else:
        return random.choice(subscribers)