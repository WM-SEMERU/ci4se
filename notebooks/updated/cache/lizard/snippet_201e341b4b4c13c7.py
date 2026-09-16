def more_like_this(self, request, pk=None):
    obj = self.get_object().object
    queryset = self.filter_queryset(self.get_queryset()).more_like_this(obj)
    page = self.paginate_queryset(queryset)
    if page is not None:
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)