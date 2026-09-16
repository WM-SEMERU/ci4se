def sens_mppt_send(self, mppt_timestamp, mppt1_volt, mppt1_amp, mppt1_pwm,
    mppt1_status, mppt2_volt, mppt2_amp, mppt2_pwm, mppt2_status,
    mppt3_volt, mppt3_amp, mppt3_pwm, mppt3_status, force_mavlink1=False):
    return self.send(self.sens_mppt_encode(mppt_timestamp, mppt1_volt,
        mppt1_amp, mppt1_pwm, mppt1_status, mppt2_volt, mppt2_amp,
        mppt2_pwm, mppt2_status, mppt3_volt, mppt3_amp, mppt3_pwm,
        mppt3_status), force_mavlink1=force_mavlink1)