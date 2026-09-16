def start_session(self, causal_consistency=True,
    default_transaction_options=None):
    return self.__start_session(False, causal_consistency=
        causal_consistency, default_transaction_options=
        default_transaction_options)