def do_refresh(self, args):
    pprint(AwsConnectionFactory.getEc2Client().describe_network_interfaces(
        NetworkInterfaceIds=[self.physicalId]))