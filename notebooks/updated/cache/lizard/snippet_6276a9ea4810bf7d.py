def wr_pydot_dag(self, fout_img, dag):
    img_fmt = os.path.splitext(fout_img)[1][1:]
    dag.write(fout_img, format=img_fmt)
    self.log.write('  {GO_USR:>3} usr {GO_ALL:>3} GOs  WROTE: {F}\n'.format
        (F=fout_img, GO_USR=len(self.gosubdag.go_sources), GO_ALL=len(dag.
        obj_dict['nodes'])))