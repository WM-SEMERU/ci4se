def ToJson(self):
    return {'assetId': self.AssetId.To0xString(), 'assetType': self.
        AssetType, 'name': self.GetName(), 'amount': self.Amount.value,
        'available': self.Available.value, 'precision': self.Precision,
        'fee': self.Fee.value, 'address': self.FeeAddress.ToString(),
        'owner': self.Owner.ToString(), 'admin': Crypto.ToAddress(self.
        Admin), 'issuer': Crypto.ToAddress(self.Issuer), 'expiration': self
        .Expiration, 'is_frozen': self.IsFrozen}