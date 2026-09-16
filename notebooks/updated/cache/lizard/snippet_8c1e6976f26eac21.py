def plot_lr(self):
    if not in_ipynb():
        plt.switch_backend('agg')
    if self.record_mom:
        fig, axs = plt.subplots(1, 2, figsize=(12, 4))
        for i in range(0, 2):
            axs[i].set_xlabel('iterations')
        axs[0].set_ylabel('learning rate')
        axs[1].set_ylabel('momentum')
        axs[0].plot(self.iterations, self.lrs)
        axs[1].plot(self.iterations, self.momentums)
    else:
        plt.xlabel('iterations')
        plt.ylabel('learning rate')
        plt.plot(self.iterations, self.lrs)
    if not in_ipynb():
        plt.savefig(os.path.join(self.save_path, 'lr_plot.png'))