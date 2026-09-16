def _reset_internal(self):
    super()._reset_internal()
    self.sim.data.qpos[self._ref_joint_pos_indexes
        ] = self.mujoco_robot.init_qpos
    if self.has_gripper:
        self.sim.data.qpos[self._ref_joint_gripper_actuator_indexes
            ] = self.gripper.init_qpos