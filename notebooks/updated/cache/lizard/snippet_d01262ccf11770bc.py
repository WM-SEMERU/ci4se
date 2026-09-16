def product(pc, service, attrib, sku):
    pc.service = service.lower()
    pc.sku = sku
    pc.add_attributes(attribs=attrib)
    click.echo('Service Alias: {0}'.format(pc.service_alias))
    click.echo('URL: {0}'.format(pc.service_url))
    click.echo('Region: {0}'.format(pc.region))
    click.echo('Product Terms: {0}'.format(pc.terms))
    click.echo('Filtering Attributes: {0}'.format(pc.attributes))
    prods = pyutu.find_products(pc)
    for p in prods:
        click.echo('Product SKU: {0} product: {1}'.format(p, json.dumps(
            prods[p], indent=2, sort_keys=True)))
    click.echo('Total Products Found: {0}'.format(len(prods)))
    click.echo('Time: {0} secs'.format(time.process_time()))