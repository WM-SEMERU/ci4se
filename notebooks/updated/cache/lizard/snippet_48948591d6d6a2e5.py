def CreateDefaultPartition(client, ad_group_id):
    ad_group_criterion_service = client.GetService('AdGroupCriterionService',
        version='v201809')
    operations = [{'operator': 'ADD', 'operand': {'xsi_type':
        'BiddableAdGroupCriterion', 'adGroupId': ad_group_id, 'criterion':
        {'xsi_type': 'ProductPartition', 'partitionType': 'UNIT'},
        'biddingStrategyConfiguration': {'bids': [{'xsi_type': 'CpcBid',
        'bid': {'microAmount': 500000}}]}}}]
    ad_group_criterion = ad_group_criterion_service.mutate(operations)['value'
        ][0]
    print(
        'Ad group criterion with ID "%d" in ad group with ID "%d" was added.' %
        (ad_group_criterion['criterion']['id'], ad_group_criterion[
        'adGroupId']))