def builds(self, request, pk=None):
    builds = self.get_object().builds.prefetch_related('test_runs').order_by(
        '-datetime')
    page = self.paginate_queryset(builds)
    serializer = BuildSerializer(page, many=True, context={'request': request})
    return self.get_paginated_response(serializer.data)