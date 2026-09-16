def _abs(ctx, number):
    return conversions.to_decimal(abs(conversions.to_decimal(number, ctx)), ctx
        )