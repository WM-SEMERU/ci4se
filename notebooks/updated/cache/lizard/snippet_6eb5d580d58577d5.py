def main(client, adgroup_id):
    adgroup_criterion_service = client.GetService('AdGroupCriterionService',
        version='v201809')
    helper = ProductPartitionHelper(adgroup_id)
    root = helper.CreateSubdivision()
    new_product_canonical_condition = {'xsi_type':
        'ProductCanonicalCondition', 'condition': 'NEW'}
    used_product_canonical_condition = {'xsi_type':
        'ProductCanonicalCondition', 'condition': 'USED'}
    other_product_canonical_condition = {'xsi_type':
        'ProductCanonicalCondition'}
    helper.CreateUnit(root, new_product_canonical_condition, 200000)
    helper.CreateUnit(root, used_product_canonical_condition, 100000)
    other_condition = helper.CreateSubdivision(root,
        other_product_canonical_condition)
    cool_product_brand = {'xsi_type': 'ProductBrand', 'value': 'CoolBrand'}
    cheap_product_brand = {'xsi_type': 'ProductBrand', 'value': 'CheapBrand'}
    other_product_brand = {'xsi_type': 'ProductBrand'}
    helper.CreateUnit(other_condition, cool_product_brand, 900000)
    helper.CreateUnit(other_condition, cheap_product_brand, 10000)
    other_brand = helper.CreateSubdivision(other_condition, other_product_brand
        )
    luggage_category = {'xsi_type': 'ProductBiddingCategory', 'type':
        'BIDDING_CATEGORY_L1', 'value': '-5914235892932915235'}
    generic_category = {'xsi_type': 'ProductBiddingCategory', 'type':
        'BIDDING_CATEGORY_L1'}
    helper.CreateUnit(other_brand, luggage_category, 750000)
    helper.CreateUnit(other_brand, generic_category, 110000)
    result = adgroup_criterion_service.mutate(helper.GetOperations())
    children = {}
    root_node = None
    for adgroup_criterion in result['value']:
        children[adgroup_criterion['criterion']['id']] = []
        if 'parentCriterionId' in adgroup_criterion['criterion']:
            children[adgroup_criterion['criterion']['parentCriterionId']
                ].append(adgroup_criterion['criterion'])
        else:
            root_node = adgroup_criterion['criterion']
    DisplayTree(root_node, children)