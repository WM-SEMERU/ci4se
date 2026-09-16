def get_tracer(self):
    sampled = self.should_sample()
    if sampled:
        self.span_context.trace_options.set_enabled(True)
        return context_tracer.ContextTracer(exporter=self.exporter,
            span_context=self.span_context)
    else:
        return noop_tracer.NoopTracer()