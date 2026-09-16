def direct_to_class(amaasclass):
    if amaasclass in ASSET:
        return CHILDREN_CLASS['asset']
    elif amaasclass in PARTY:
        return CHILDREN_CLASS['party']
    elif amaasclass in TRANSACTION:
        return CHILDREN_CLASS['transaction']
    elif amaasclass in BOOK:
        return CHILDREN_CLASS['book']
    elif amaasclass in CORPORATE_ACTION:
        return CHILDREN_CLASS['corporate_action']
    elif amaasclass in MARKET_DATA:
        return None
    else:
        return CHILDREN_CLASS['asset_manager']