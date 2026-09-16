def micro_calc(TP, item):
    try:
        TP_sum = sum(TP.values())
        item_sum = sum(item.values())
        return TP_sum / (TP_sum + item_sum)
    except Exception:
        return 'None'