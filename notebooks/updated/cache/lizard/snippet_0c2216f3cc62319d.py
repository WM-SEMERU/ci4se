def run_args(self):
    self.arg_parser = self._parse_args()
    self.args = self.arg_parser.parse_args()
    color_name = self.args.color
    if color_name is not None:
        color_name = color_name[0]
    symbol = self.args.symbol
    try:
        self.tr(symbol, color_name)
    except InvalidColorException:
        print('Invalid Color Name!')