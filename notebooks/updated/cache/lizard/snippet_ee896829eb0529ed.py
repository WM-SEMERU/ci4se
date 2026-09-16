def simxSetJointPosition(clientID, jointHandle, position, operationMode):
    return c_SetJointPosition(clientID, jointHandle, position, operationMode)