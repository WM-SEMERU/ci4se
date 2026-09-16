def wants_rdf(self, accepts):
    mimetype = mimeparse.best_match(all_mimetypes + self.all_mimetypes + [
        WILDCARD], accepts)
    return mimetype and mimetype != WILDCARD