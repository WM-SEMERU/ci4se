def get_token(self, request):
    return stripe.Token.create(card={'number': request.data['number'],
        'exp_month': request.data['exp_month'], 'exp_year': request.data[
        'exp_year'], 'cvc': request.data['cvc']})