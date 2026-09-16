def _get_demand_array_construct(self):
    bus_no = integer.setResultsName('bus_no')
    s_rating = real.setResultsName('s_rating')
    p_direction = real.setResultsName('p_direction')
    q_direction = real.setResultsName('q_direction')
    p_bid_max = real.setResultsName('p_bid_max')
    p_bid_min = real.setResultsName('p_bid_min')
    p_optimal_bid = Optional(real).setResultsName('p_optimal_bid')
    p_fixed = real.setResultsName('p_fixed')
    p_proportional = real.setResultsName('p_proportional')
    p_quadratic = real.setResultsName('p_quadratic')
    q_fixed = real.setResultsName('q_fixed')
    q_proportional = real.setResultsName('q_proportional')
    q_quadratic = real.setResultsName('q_quadratic')
    commitment = boolean.setResultsName('commitment')
    cost_tie_break = real.setResultsName('cost_tie_break')
    cost_cong_up = real.setResultsName('cost_cong_up')
    cost_cong_down = real.setResultsName('cost_cong_down')
    status = Optional(boolean).setResultsName('status')
    demand_data = (bus_no + s_rating + p_direction + q_direction +
        p_bid_max + p_bid_min + p_optimal_bid + p_fixed + p_proportional +
        p_quadratic + q_fixed + q_proportional + q_quadratic + commitment +
        cost_tie_break + cost_cong_up + cost_cong_down + status + scolon)
    demand_data.setParseAction(self.push_demand)
    demand_array = Literal('Demand.con') + '=' + '[' + '...' + ZeroOrMore(
        demand_data + Optional(']' + scolon))
    return demand_array