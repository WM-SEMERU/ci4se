def layout_asides(self, block, context, frag, view_name, aside_frag_fns):
    result = Fragment(frag.content)
    result.add_fragment_resources(frag)
    for aside, aside_fn in aside_frag_fns:
        aside_frag = self.wrap_aside(block, aside, view_name, aside_fn(
            block, context), context)
        aside.save()
        result.add_content(aside_frag.content)
        result.add_fragment_resources(aside_frag)
    return result