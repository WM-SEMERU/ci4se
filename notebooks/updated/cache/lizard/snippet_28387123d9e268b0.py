def js_link(self, attr, other, other_attr):
    if attr not in self.properties():
        raise ValueError('%r is not a property of self (%r)' % (attr, self))
    if not isinstance(other, Model):
        raise ValueError("'other' is not a Bokeh model: %r" % other)
    if other_attr not in other.properties():
        raise ValueError('%r is not a property of other (%r)' % (other_attr,
            other))
    from bokeh.models.callbacks import CustomJS
    cb = CustomJS(args=dict(other=other), code='other.%s = this.%s' % (
        other_attr, attr))
    self.js_on_change(attr, cb)