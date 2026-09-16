def do_terminateInstance(self, args):
    parser = CommandArgumentParser('terminateInstance')
    parser.add_argument(dest='instance', help='instance index or name')
    args = vars(parser.parse_args(args))
    instanceId = args['instance']
    try:
        index = int(instanceId)
        instances = self.scalingGroupDescription['AutoScalingGroups'][0][
            'Instances']
        instanceId = instances[index]
    except ValueError:
        pass
    client = AwsConnectionFactory.getEc2Client()
    client.terminate_instances(InstanceIds=[instanceId['InstanceId']])
    self.do_printInstances('-r')