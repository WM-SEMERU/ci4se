def get_alerts_on(self, weather_param):
    result = []
    for alert in self.alerts:
        for met_condition in alert.met_conditions:
            if met_condition['condition'].weather_param == weather_param:
                result.append(alert)
                break
    return result