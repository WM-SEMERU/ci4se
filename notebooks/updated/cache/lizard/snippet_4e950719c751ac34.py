def paid_totals_for(self, year, month):
    return self.during(year, month).aggregate(total_amount=models.Sum('amount')
        )