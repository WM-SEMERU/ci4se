def get_stripe_dashboard_url(self):
    if not self.stripe_dashboard_item_name or not self.id:
        return ''
    else:
        return '{base_url}{item}/{id}'.format(base_url=self.
            _get_base_stripe_dashboard_url(), item=self.
            stripe_dashboard_item_name, id=self.id)