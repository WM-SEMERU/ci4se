def _reset_internal(self):
    super()._reset_internal()
    self.sim.data.qpos[self._ref_joint_pos_indexes
        ] = self.mujoco_robot.init_qpos
    if self.has_gripper_right:
        self.sim.data.qpos[self._ref_joint_gripper_right_actuator_indexes
            ] = self.gripper_right.init_qpos
    if self.has_gripper_left:
        self.sim.data.qpos[self._ref_joint_gripper_left_actuator_indexes
            ] = self.gripper_left.init_qpos