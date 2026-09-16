def _get_slack_array_construct(self):
    bus_no = integer.setResultsName('bus_no')
    s_rating = real.setResultsName('s_rating')
    v_rating = real.setResultsName('v_rating')
    v_magnitude = real.setResultsName('v_magnitude')
    ref_angle = real.setResultsName('ref_angle')
    q_max = Optional(real).setResultsName('q_max')
    q_min = Optional(real).setResultsName('q_min')
    v_max = Optional(real).setResultsName('v_max')
    v_min = Optional(real).setResultsName('v_min')
    p_guess = Optional(real).setResultsName('p_guess')
    lp_coeff = Optional(real).setResultsName('lp_coeff')
    ref_bus = Optional(boolean).setResultsName('ref_bus')
    status = Optional(boolean).setResultsName('status')
    slack_data = (bus_no + s_rating + v_rating + v_magnitude + ref_angle +
        q_max + q_min + v_max + v_min + p_guess + lp_coeff + ref_bus +
        status + scolon)
    slack_data.setParseAction(self.push_slack)
    slack_array = Literal('SW.con') + '=' + '[' + '...' + ZeroOrMore(
        slack_data + Optional(']' + scolon))
    return slack_array