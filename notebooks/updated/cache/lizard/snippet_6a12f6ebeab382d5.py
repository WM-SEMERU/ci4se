def IsPayable(self):
    from neo.Core.State.ContractState import ContractPropertyState
    return self.ContractProperties & ContractPropertyState.Payable > 0