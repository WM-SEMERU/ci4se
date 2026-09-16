def parseDEI(self, xbrl, ignore_errors=0):
    dei_obj = DEI()
    if ignore_errors == 2:
        logging.basicConfig(filename='/tmp/xbrl.log', level=logging.ERROR,
            format='%(asctime)s %(levelname)s %(name)s %(message)s')
        logger = logging.getLogger(__name__)
    else:
        logger = None
    trading_symbol = xbrl.find_all(name=re.compile('(dei:tradingsymbol)', 
        re.IGNORECASE | re.MULTILINE))
    dei_obj.trading_symbol = self.data_processing(trading_symbol, xbrl,
        ignore_errors, logger, options={'type': 'String', 'no_context': True})
    company_name = xbrl.find_all(name=re.compile(
        '(dei:entityregistrantname)', re.IGNORECASE | re.MULTILINE))
    dei_obj.company_name = self.data_processing(company_name, xbrl,
        ignore_errors, logger, options={'type': 'String', 'no_context': True})
    shares_outstanding = xbrl.find_all(name=re.compile(
        '(dei:entitycommonstocksharesoutstanding)', re.IGNORECASE | re.
        MULTILINE))
    dei_obj.shares_outstanding = self.data_processing(shares_outstanding,
        xbrl, ignore_errors, logger, options={'type': 'Number',
        'no_context': True})
    public_float = xbrl.find_all(name=re.compile('(dei:entitypublicfloat)',
        re.IGNORECASE | re.MULTILINE))
    dei_obj.public_float = self.data_processing(public_float, xbrl,
        ignore_errors, logger, options={'type': 'Number', 'no_context': True})
    return dei_obj