def clean_total_refund_amount(self):
    initial = self.cleaned_data.get('initial_refund_amount', 0)
    total = self.cleaned_data['total_refund_amount']
    summed_refunds = sum([v for k, v in self.cleaned_data.items() if k.
        startswith('item_refundamount_')])
    if not self.cleaned_data.get('id'):
        raise ValidationError('ID not in cleaned data')
    if summed_refunds != total:
        raise ValidationError(_(
            'Passed value does not match sum of allocated refunds.'))
    elif summed_refunds > self.cleaned_data['id'
        ].amountPaid + self.cleaned_data['id'].refunds:
        raise ValidationError(_(
            'Total refunds allocated exceed revenue received.'))
    elif total < initial:
        raise ValidationError(_(
            'Cannot reduce the total amount of the refund.'))
    return total