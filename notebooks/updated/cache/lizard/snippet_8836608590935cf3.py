def on_delete(resc, req, resp, rid):
    signals.pre_req.send(resc.model)
    signals.pre_req_delete.send(resc.model)
    model = find(resc.model, rid)
    goldman.sess.store.delete(model)
    resp.status = falcon.HTTP_204
    signals.post_req.send(resc.model)
    signals.post_req_delete.send(resc.model)