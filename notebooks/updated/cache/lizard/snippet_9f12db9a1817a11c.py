def main():
    items = [Item('Name1', 'Description1'), Item('Name2', 'Description2'),
        Item('Name3', 'Description3')]
    table = ItemTable(items)
    print(table.__html__())