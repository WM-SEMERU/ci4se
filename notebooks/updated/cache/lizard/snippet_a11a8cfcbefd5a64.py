def on_drag(self, cursor_x, cursor_y):
    from blmath.geometry.transform.rodrigues import as_rotation_matrix
    if self.isdragging:
        mouse_pt = arcball.Point2fT(cursor_x, cursor_y)
        ThisQuat = self.arcball.drag(mouse_pt)
        self.thisrot = arcball.Matrix3fSetRotationFromQuat4f(ThisQuat)
        self.thisrot = arcball.Matrix3fMulMatrix3f(self.lastrot, self.thisrot)
        self.thisrot = as_rotation_matrix(self.thisrot)
        self.transform = arcball.Matrix4fSetRotationFromMatrix3f(self.
            transform, self.thisrot)
        glut.glutPostRedisplay()
    return