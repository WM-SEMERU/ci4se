async def disconnect(self, sid, namespace=None):
    namespace = namespace or '/'
    if self.manager.is_connected(sid, namespace=namespace):
        self.logger.info('Disconnecting %s [%s]', sid, namespace)
        self.manager.pre_disconnect(sid, namespace=namespace)
        await self._send_packet(sid, packet.Packet(packet.DISCONNECT,
            namespace=namespace))
        await self._trigger_event('disconnect', namespace, sid)
        self.manager.disconnect(sid, namespace=namespace)