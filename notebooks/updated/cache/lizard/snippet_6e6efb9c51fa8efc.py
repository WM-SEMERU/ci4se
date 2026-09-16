def download(client, target_dir):
    print('')
    print('download inappproducts')
    print('---------------------')
    products = client.list_inappproducts()
    for product in products:
        path = os.path.join(target_dir, 'products')
        del product['packageName']
        mkdir_p(path)
        with open(os.path.join(path, product['sku'] + '.json'), 'w'
            ) as outfile:
            print('save product for {0}'.format(product['sku']))
            json.dump(product, outfile, sort_keys=True, indent=4,
                separators=(',', ': '))