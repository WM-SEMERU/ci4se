def get_motor_force(self, motor_name):
    return self.call_remote_api('simxGetJointForce', self.get_object_handle
        (motor_name), streaming=True)