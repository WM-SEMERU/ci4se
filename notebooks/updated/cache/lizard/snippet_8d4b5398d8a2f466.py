def android_example():
    env = holodeck.make('AndroidPlayground')
    command = np.ones(94) * 10
    for i in range(10):
        env.reset()
        for j in range(1000):
            if j % 50 == 0:
                command *= -1
            state, reward, terminal, _ = env.step(command)
            pixels = state[Sensors.PIXEL_CAMERA]
            orientation = state[Sensors.ORIENTATION_SENSOR]