def get_agreement(self, agreement_id):
    agreement = self.contract_concise.getAgreement(agreement_id)
    if agreement and len(agreement) == 6:
        agreement = AgreementValues(*agreement)
        did = add_0x_prefix(agreement.did.hex())
        cond_ids = [add_0x_prefix(_id.hex()) for _id in agreement.condition_ids
            ]
        return AgreementValues(did, agreement.owner, agreement.template_id,
            cond_ids, agreement.updated_by, agreement.block_number_updated)
    return None