def demo(printer, **kwargs):
    for demo_choice in kwargs.keys():
        command = getattr(printer, demo_choice.replace('barcodes_a',
            'barcode').replace('barcodes_b', 'barcode'))
        for params in DEMO_FUNCTIONS[demo_choice]:
            command(**params)
        printer.cut()