def start(self):
    self._events_to_write = []
    self._new_contracts_to_write = []

    @events.on(SmartContractEvent.CONTRACT_CREATED)
    @events.on(SmartContractEvent.CONTRACT_MIGRATED)
    def call_on_success_event(sc_event: SmartContractEvent):
        self.on_smart_contract_created(sc_event)

    @events.on(SmartContractEvent.RUNTIME_NOTIFY)
    def call_on_event(sc_event: NotifyEvent):
        self.on_smart_contract_event(sc_event)
    Blockchain.Default(
        ).PersistCompleted.on_change += self.on_persist_completed