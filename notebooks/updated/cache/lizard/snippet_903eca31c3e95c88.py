def search(self, name=None, category=None, description=None, price=None,
    price__gt=None, price__gte=None, price__lt=None, price__lte=None,
    location=(None, None), radius=None, tl_coord=(None, None), br_coord=(
    None, None), country=None, locality=None, region=None, postal_code=None,
    street_address=None, website_url=None):
    params = self._get_params(name=name, description=description, price=
        price, price__gt=price__gt, price__gte=price__gte, price__lt=
        price__lt, price__lte=price__lte, location=location, radius=radius,
        tl_coord=tl_coord, br_coord=br_coord, country=country, locality=
        locality, region=region, postal_code=postal_code, street_address=
        street_address, website_url=website_url)
    return self._create_query('search', params)