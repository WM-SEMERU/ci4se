def delete(self, request, **kwargs):
    try:
        customer, _created = Customer.get_or_create(subscriber=
            subscriber_request_callback(self.request))
        customer.subscription.cancel(at_period_end=CANCELLATION_AT_PERIOD_END)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception:
        return Response('Something went wrong cancelling the subscription.',
            status=status.HTTP_400_BAD_REQUEST)