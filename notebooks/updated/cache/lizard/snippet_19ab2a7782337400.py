def load_configs(self):
    if self.config is None:
        return False
    if 'monitor' in self.config.sections():
        logger.warning(
            'A deprecated [monitor] section exists in the Glances configuration file. You should use the new Applications Monitoring Process module instead (http://glances.readthedocs.io/en/develop/aoa/amps.html).'
            )
    header = 'glances_'
    for s in self.config.sections():
        if s.startswith('amp_'):
            amp_conf_name = s[4:]
            amp_script = os.path.join(amps_path, header + s[4:] + '.py')
            if not os.path.exists(amp_script):
                amp_script = os.path.join(amps_path, 'glances_default.py')
            try:
                amp = __import__(os.path.basename(amp_script)[:-3])
            except ImportError as e:
                logger.warning('Missing Python Lib ({}), cannot load {} AMP'
                    .format(e, amp_conf_name))
            except Exception as e:
                logger.warning('Cannot load {} AMP ({})'.format(
                    amp_conf_name, e))
            else:
                self.__amps_dict[amp_conf_name] = amp.Amp(name=
                    amp_conf_name, args=self.args)
                self.__amps_dict[amp_conf_name].load_config(self.config)
    logger.debug('AMPs list: {}'.format(self.getList()))
    return True