def update_payTo(apps, schema_editor):
    TransactionParty = apps.get_model('financial', 'TransactionParty')
    ExpenseItem = apps.get_model('financial', 'ExpenseItem')
    RevenueItem = apps.get_model('financial', 'RevenueItem')
    GenericRepeatedExpense = apps.get_model('financial',
        'GenericRepeatedExpense')
    for item in chain(ExpenseItem.objects.filter(Q(payToUser__isnull=False) |
        Q(payToLocation__isnull=False) | Q(payToName__isnull=False)),
        GenericRepeatedExpense.objects.filter(Q(payToUser__isnull=False) |
        Q(payToLocation__isnull=False) | Q(payToName__isnull=False))):
        if getattr(item, 'payToUser', None):
            party = TransactionParty.objects.get_or_create(user=item.
                payToUser, defaults={'name': getFullName(item.payToUser),
                'staffMember': getattr(item.payToUser, 'staffmember', None)})[0
                ]
        elif getattr(item, 'payToLocation', None):
            party = TransactionParty.objects.get_or_create(location=item.
                payToLocation, defaults={'name': item.payToLocation.name})[0]
        elif getattr(item, 'payToName', None):
            party = createPartyFromName(apps, item.payToName)
        item.payTo = party
        item.save()
    for item in RevenueItem.objects.filter(Q(receivedFromName__isnull=False)):
        party = createPartyFromName(apps, item.receivedFromName)
        item.receivedFrom = party
        item.save()