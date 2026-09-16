def calculate(self, variable_name, period, **parameters):
    population = self.get_variable_population(variable_name)
    holder = population.get_holder(variable_name)
    variable = self.tax_benefit_system.get_variable(variable_name,
        check_existence=True)
    if period is not None and not isinstance(period, periods.Period):
        period = periods.period(period)
    if self.trace:
        self.tracer.record_calculation_start(variable.name, period, **
            parameters)
    self._check_period_consistency(period, variable)
    cached_array = holder.get_array(period)
    if cached_array is not None:
        if self.trace:
            self.tracer.record_calculation_end(variable.name, period,
                cached_array, **parameters)
        return cached_array
    array = None
    try:
        self._check_for_cycle(variable, period)
        array = self._run_formula(variable, population, period)
        if array is None:
            array = holder.default_array()
        array = self._cast_formula_result(array, variable)
        holder.put_in_cache(array, period)
    except SpiralError:
        array = holder.default_array()
    finally:
        if self.trace:
            self.tracer.record_calculation_end(variable.name, period, array,
                **parameters)
        self._clean_cycle_detection_data(variable.name)
    self.purge_cache_of_invalid_values()
    return array