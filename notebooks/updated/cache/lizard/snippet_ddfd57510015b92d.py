def _run_xmlsec(self, com_list, extra_args):
    with NamedTemporaryFile(suffix='.xml', delete=self._xmlsec_delete_tmpfiles
        ) as ntf:
        com_list.extend(['--output', ntf.name])
        com_list += extra_args
        logger.debug('xmlsec command: %s', ' '.join(com_list))
        pof = Popen(com_list, stderr=PIPE, stdout=PIPE)
        p_out, p_err = pof.communicate()
        p_out = p_out.decode()
        p_err = p_err.decode()
        if pof.returncode != 0:
            errmsg = 'returncode={code}\nerror={err}\noutput={out}'.format(code
                =pof.returncode, err=p_err, out=p_out)
            logger.error(errmsg)
            raise XmlsecError(errmsg)
        ntf.seek(0)
        return p_out, p_err, ntf.read()