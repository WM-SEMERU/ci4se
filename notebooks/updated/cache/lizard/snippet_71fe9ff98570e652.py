def get_basket_items(request):
    bid = basket_id(request)
    return BasketItem.objects.filter(basket_id=bid), bid