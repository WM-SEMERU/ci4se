def cancel_bundle_task(self, bundle_id):
    params = {'BundleId': bundle_id}
    return self.get_object('CancelBundleTask', params, BundleInstanceTask,
        verb='POST')