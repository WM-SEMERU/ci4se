def breathe_lights(self, color, selector='all', from_color=None, period=1.0,
    cycles=1.0, persist=False, power_on=True, peak=0.5):
    argument_tuples = [('color', color), ('from_color', from_color), (
        'period', period), ('cycles', cycles), ('persist', persist), (
        'power_on', power_on), ('peak', peak)]
    return self.client.perform_request(method='post', endpoint=
        'lights/{}/effects/breathe', endpoint_args=[selector],
        argument_tuples=argument_tuples)