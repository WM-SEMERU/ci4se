def GetFeedItemIdsForCampaign(campaign_feed):
    feed_item_ids = set()
    try:
        lhs_operand = campaign_feed['matchingFunction']['lhsOperand']
    except KeyError:
        lhs_operand = None
    if lhs_operand and lhs_operand[0]['FunctionArgumentOperand.Type'
        ] == 'RequestContextOperand':
        request_context_operand = lhs_operand[0]
        if request_context_operand['contextType'
            ] == 'FEED_ITEM_ID' and campaign_feed['matchingFunction'][
            'operator'] == 'IN':
            for argument in campaign_feed['matchingFunction']['rhsOperand']:
                if argument['xsi_type'] == 'ConstantOperand':
                    feed_item_ids.add(argument['longValue'])
    return feed_item_ids