def update(customer, **data):
    if isinstance(customer, resources.Customer):
        customer = customer.id
    http_client = HttpClient()
    response, _ = http_client.patch(routes.url(routes.CUSTOMER_RESOURCE,
        resource_id=customer), data)
    return resources.Customer(**response)