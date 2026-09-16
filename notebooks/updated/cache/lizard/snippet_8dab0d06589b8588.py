def __managed_policy_map(self):
    try:
        iam_client = boto3.client('iam')
        return ManagedPolicyLoader(iam_client).load()
    except Exception as ex:
        if self._offline_fallback:
            with open(self._DEFAULT_MANAGED_POLICIES_FILE, 'r') as fp:
                return json.load(fp)
        raise ex