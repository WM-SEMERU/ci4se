def visitInlineShapeExpression(self, ctx: ShExDocParser.
    InlineShapeExpressionContext):
    expr_parser = ShexShapeExpressionParser(self.context)
    expr_parser.visitChildren(ctx)
    self.expression.valueExpr = expr_parser.expr