def get_primary_contributors(self, permitted=False):
    primary_credits = []
    credits = self.credits.exclude(credit_option=None,
        credit_option__role_priority=None).order_by(
        'credit_option__role_priority')
    if credits.exists():
        primary_priority = credits[0].credit_option.role_priority
        for credit in credits:
            if credit.credit_option.role_priority == primary_priority:
                primary_credits.append(credit)
    contributors = []
    for credit in primary_credits:
        contributor = credit.contributor
        if (permitted == False or permitted == True and contributor.
            is_permitted):
            contributors.append(contributor)
    return contributors