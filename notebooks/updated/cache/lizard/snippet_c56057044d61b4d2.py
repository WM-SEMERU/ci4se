def get_motor_position(self, motor_name):
    return self.call_remote_api('simxGetJointPosition', self.
        get_object_handle(motor_name), streaming=True)