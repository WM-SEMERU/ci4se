async def enable_digital_reporting(self, pin):
    port = pin // 8
    command = [PrivateConstants.REPORT_DIGITAL + port, PrivateConstants.
        REPORTING_ENABLE]
    await self._send_command(command)