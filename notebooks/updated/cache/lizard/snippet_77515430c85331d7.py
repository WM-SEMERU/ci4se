def process_request(self, req, resp):
    goldman.sess.req = req
    if goldman.config.STORE:
        goldman.sess.store = goldman.config.STORE()