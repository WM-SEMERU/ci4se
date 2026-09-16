def put_everything_together(self):
    molecule_list = [self.filestart] + [self.white_circles] + [self.
        draw_molecule] + [self.draw.draw_hbonds] + [self.draw.draw_pi_lines
        ] + [self.draw.draw_saltbridges] + [self.draw.cloud] + [self.draw_plots
        ] + [self.end_symbol]
    self.final_molecule = ''.join(map(str, molecule_list))