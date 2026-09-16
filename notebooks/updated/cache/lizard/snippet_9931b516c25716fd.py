def pubkey(self):
    if not self.is_public:
        if self._sibling is None or isinstance(self._sibling, weakref.ref):
            pub = PGPKey()
            pub.ascii_headers = self.ascii_headers.copy()
            pub._key = self._key.pubkey()
            for skid, subkey in self.subkeys.items():
                pub |= subkey.pubkey
            for uid in self._uids:
                pub |= copy.copy(uid)
            for sig in self._signatures:
                if sig.parent is None:
                    pub |= copy.copy(sig)
            self._sibling = weakref.ref(pub)
            pub._sibling = weakref.ref(self)
        return self._sibling()
    return None