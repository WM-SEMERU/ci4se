async def _send_button_template(self, request: Request, stack: Stack):
    gt = stack.get_layer(ButtonTemplate)
    payload = {'template_type': 'button', 'text': await render(gt.text,
        request), 'buttons': [(await b.serialize(request)) for b in gt.buttons]
        }
    msg = {'attachment': {'type': 'template', 'payload': payload}}
    await self._add_qr(stack, msg, request)
    await self._send(request, msg, stack)