def download_bundle_view(self, request, pk):
    return self._download_response(request, pk, bundle=True)