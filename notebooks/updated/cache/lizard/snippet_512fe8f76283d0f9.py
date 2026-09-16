def disco_query(self):
    return_url = self.sp.config.getattr('endpoints', 'sp')['discovery_response'
        ][0][0]
    loc = self.sp.create_discovery_service_request(self.discosrv, self.sp.
        config.entityid, **{'return': return_url})
    return SeeOther(loc)