def export_symbols(self):
    session = self.open_session()
    links = session.query(AssetClassStock).order_by(AssetClassStock.symbol
        ).all()
    output = []
    for link in links:
        output.append(link.symbol + '\n')
    with open('symbols.txt', mode='w') as file:
        file.writelines(output)
    print('Symbols exported to symbols.txt')