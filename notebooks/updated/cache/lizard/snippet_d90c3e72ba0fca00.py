def _chunk_getitem(self, chunk_coords, chunk_selection, out, out_selection,
    drop_axes=None, fields=None):
    assert len(chunk_coords) == len(self._cdata_shape)
    ckey = self._chunk_key(chunk_coords)
    try:
        cdata = self.chunk_store[ckey]
    except KeyError:
        if self._fill_value is not None:
            if fields:
                fill_value = self._fill_value[fields]
            else:
                fill_value = self._fill_value
            out[out_selection] = fill_value
    else:
        if isinstance(out, np.ndarray
            ) and not fields and is_contiguous_selection(out_selection
            ) and is_total_slice(chunk_selection, self._chunks
            ) and not self._filters and self._dtype != object:
            dest = out[out_selection]
            write_direct = dest.flags.writeable and (self._order == 'C' and
                dest.flags.c_contiguous or self._order == 'F' and dest.
                flags.f_contiguous)
            if write_direct:
                if self._compressor:
                    self._compressor.decode(cdata, dest)
                else:
                    chunk = ensure_ndarray(cdata).view(self._dtype)
                    chunk = chunk.reshape(self._chunks, order=self._order)
                    np.copyto(dest, chunk)
                return
        chunk = self._decode_chunk(cdata)
        if fields:
            chunk = chunk[fields]
        tmp = chunk[chunk_selection]
        if drop_axes:
            tmp = np.squeeze(tmp, axis=drop_axes)
        out[out_selection] = tmp