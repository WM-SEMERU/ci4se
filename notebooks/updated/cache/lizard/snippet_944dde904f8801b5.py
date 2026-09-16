def _read_weights(self):
    weights = []
    grams_per_pound = 453.592
    for ser in self._serials:
        ser.write('W\r')
        ser.flush()
    time.sleep(0.02)
    for ser in self._serials:
        try:
            output_str = ser.readline()
            weight = float(output_str) * grams_per_pound
            weights.append(weight)
        except:
            weights.append(0.0)
    log_output = ''
    for w in weights:
        log_output += '{:.2f} '.format(w)
    rospy.loginfo(log_output)
    return weights