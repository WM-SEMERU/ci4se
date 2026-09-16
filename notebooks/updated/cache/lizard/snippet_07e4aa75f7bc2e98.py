def render(self, context, instance, placeholder):
    if instance and instance.template:
        self.render_template = instance.template
    return super(PluginTemplateMixin, self).render(context, instance,
        placeholder)