def get_service_info(self):
    postresult = requests.get('%s://%s/ga4gh/wes/v1/service-info' % (self.
        proto, self.host), headers=self.auth)
    return wes_reponse(postresult)