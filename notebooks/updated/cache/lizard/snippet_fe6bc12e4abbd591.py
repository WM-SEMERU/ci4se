def is_supported(self, user_agent_string):
    user_agent_obj = user_agents.parse(user_agent_string)
    browser_ok = True
    for rule in self.exclusions:
        if rule in ['mobile', 'tablet', 'touchcapable', 'pc', 'bot']:
            if (rule == 'mobile' and user_agent_obj.is_mobile or rule ==
                'tablet' and user_agent_obj.is_tablet or rule ==
                'touchcapable' and user_agent_obj.is_touch_capable or rule ==
                'pc' and user_agent_obj.is_pc or rule == 'bot' and
                user_agent_obj.is_bot):
                browser_ok = False
        elif rule in user_agent_string:
            browser_ok = False
    return browser_ok