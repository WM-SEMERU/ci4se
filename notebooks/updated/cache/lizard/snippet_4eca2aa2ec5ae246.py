def create_grad(node, namer, tangent=False):
    if not isinstance(node, (gast.Subscript, gast.Name, gast.Str)):
        raise TypeError
    if anno.hasanno(node, 'temp_var'):
        return create_grad(anno.getanno(node, 'temp_var'), namer, tangent)

    def _name_grad(node):
        if not isinstance(node, gast.Name):
            raise TypeError
        varname = node.id
        name = namer.grad(varname, tangent)
        grad_node = gast.Name(id=name, ctx=None, annotation=None)
        anno.setanno(grad_node, 'adjoint_var', node)
        return grad_node
    if isinstance(node, gast.Subscript):
        grad_node = create_grad(node.value, namer, tangent=tangent)
        grad_node.ctx = gast.Load()
        return gast.Subscript(value=grad_node, slice=node.slice, ctx=None)
    elif isinstance(node, gast.Str):
        grad_node = create_grad(gast.Name(id=node.s, ctx=None, annotation=
            None), namer, tangent=tangent)
        return gast.Str(grad_node.id)
    else:
        return _name_grad(node)