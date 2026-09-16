def load_data_batch(self, data_batch):
    if self.sym_gen is not None:
        key = data_batch.bucket_key
        if key not in self.execgrp_bucket:
            symbol = self.sym_gen(key)
            execgrp = DataParallelExecutorGroup(symbol, self.arg_names,
                self.param_names, self.ctx, self.slices, data_batch,
                shared_group=self.execgrp)
            self.execgrp_bucket[key] = execgrp
        self.curr_execgrp = self.execgrp_bucket[key]
    else:
        self.curr_execgrp = self.execgrp
    self.curr_execgrp.load_data_batch(data_batch)