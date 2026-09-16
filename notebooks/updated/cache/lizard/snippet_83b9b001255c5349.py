def track_purchase(self, user, items, total, purchase_id=None, campaign_id=
    None, template_id=None, created_at=None, data_fields=None):
    call = '/api/commerce/trackPurchase'
    payload = {}
    if isinstance(user, dict):
        payload['user'] = user
    else:
        raise TypeError('user key is not in Dictionary format')
    if isinstance(items, list):
        payload['items'] = items
    else:
        raise TypeError('items are not in Array format')
    if isinstance(total, float):
        payload['total'] = total
    else:
        raise TypeError('total is not in correct format')
    if purchase_id is not None:
        payload['id'] = str(purchase_id)
    if campaign_id is not None:
        payload['campaignId'] = campaign_id
    if template_id is not None:
        payload['templateId'] = template_id
    if created_at is not None:
        payload['createdAt'] = created_at
    if data_fields is not None:
        payload['data_fields'] = data_fields
    return self.api_call(call=call, method='POST', json=payload)