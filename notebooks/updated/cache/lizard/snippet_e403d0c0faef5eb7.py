def reset(self):
    self._target_by_address = OrderedDict()
    self._target_dependencies_by_address = defaultdict(OrderedSet)
    self._target_dependees_by_address = defaultdict(OrderedSet)
    self._derived_from_by_derivative = {}
    self._derivatives_by_derived_from = defaultdict(list)
    self.synthetic_addresses = set()