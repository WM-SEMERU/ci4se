def is_all_field_none(self):
    if self._id_ is not None:
        return False
    if self._created is not None:
        return False
    if self._updated is not None:
        return False
    if self._time_responded is not None:
        return False
    if self._time_expiry is not None:
        return False
    if self._time_refund_requested is not None:
        return False
    if self._time_refunded is not None:
        return False
    if self._user_refund_requested is not None:
        return False
    if self._monetary_account_id is not None:
        return False
    if self._amount_inquired is not None:
        return False
    if self._amount_responded is not None:
        return False
    if self._status is not None:
        return False
    if self._description is not None:
        return False
    if self._alias is not None:
        return False
    if self._counterparty_alias is not None:
        return False
    if self._attachment is not None:
        return False
    if self._minimum_age is not None:
        return False
    if self._require_address is not None:
        return False
    if self._geolocation is not None:
        return False
    if self._type_ is not None:
        return False
    if self._sub_type is not None:
        return False
    if self._redirect_url is not None:
        return False
    if self._address_billing is not None:
        return False
    if self._address_shipping is not None:
        return False
    if self._allow_chat is not None:
        return False
    if self._credit_scheme_identifier is not None:
        return False
    if self._mandate_identifier is not None:
        return False
    if self._eligible_whitelist_id is not None:
        return False
    if self._request_reference_split_the_bill is not None:
        return False
    return True