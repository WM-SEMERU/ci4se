def dispatch(self, *args, **kwargs):
    try:
        self.auth(*args, **kwargs)
        return super(RestView, self).dispatch(*args, **kwargs)
    except ValidationError as e:
        return self.render_to_response(e.message_dict, status=409)
    except Http404 as e:
        return self.render_to_response(str(e), status=404)
    except PermissionDenied as e:
        return self.render_to_response(str(e), status=403)
    except ValueError as e:
        return self.render_to_response(str(e), status=400)