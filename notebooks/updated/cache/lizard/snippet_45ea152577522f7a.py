def registerThermostat(self, thermostat):
    try:
        type(thermostat) == heatmiser.HeatmiserThermostat
        if thermostat.address in self.thermostats.keys():
            raise ValueError('Key already present')
        else:
            self.thermostats[thermostat.address] = thermostat
    except ValueError:
        pass
    except Exception as e:
        logging.info("You're not adding a HeatmiiserThermostat Object")
        logging.info(e.message)
    return self._serport