def Serialize(self, writer):
    super(SpentCoinState, self).Serialize(writer)
    writer.WriteUInt256(self.TransactionHash)
    writer.WriteUInt32(self.TransactionHeight)
    writer.WriteVarInt(len(self.Items))
    for item in self.Items:
        writer.WriteUInt16(item.index)
        writer.WriteUInt32(item.height)