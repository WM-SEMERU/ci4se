def reliability_curve(self):
    total = self.frequencies['Total_Freq'].sum()
    curve = pd.DataFrame(columns=['Bin_Start', 'Bin_End', 'Bin_Center',
        'Positive_Relative_Freq', 'Total_Relative_Freq'])
    curve['Bin_Start'] = self.thresholds[:-1]
    curve['Bin_End'] = self.thresholds[1:]
    curve['Bin_Center'] = 0.5 * (self.thresholds[:-1] + self.thresholds[1:])
    curve['Positive_Relative_Freq'] = self.frequencies['Positive_Freq'
        ] / self.frequencies['Total_Freq']
    curve['Total_Relative_Freq'] = self.frequencies['Total_Freq'] / total
    return curve