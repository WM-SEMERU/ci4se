def max_bit_rate(self):
    status = self.fc.call_action('WANCommonInterfaceConfig',
        'GetCommonLinkProperties')
    downstream = status['NewLayer1DownstreamMaxBitRate']
    upstream = status['NewLayer1UpstreamMaxBitRate']
    return upstream, downstream