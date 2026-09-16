def calculate_per_unit_commission(order, transaction, cost_per_unit,
    initial_commission, min_trade_cost):
    additional_commission = abs(transaction.amount * cost_per_unit)
    if order.commission == 0:
        return max(min_trade_cost, additional_commission + initial_commission)
    else:
        per_unit_total = abs(order.filled * cost_per_unit
            ) + additional_commission + initial_commission
        if per_unit_total < min_trade_cost:
            return 0
        else:
            return per_unit_total - order.commission