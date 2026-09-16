def finalize(self, **kwargs):
    self.set_title('ROC Curves for {}'.format(self.name))
    self.ax.legend(loc='lower right', frameon=True)
    self.ax.set_xlim([0.0, 1.0])
    self.ax.set_ylim([0.0, 1.0])
    self.ax.set_ylabel('True Postive Rate')
    self.ax.set_xlabel('False Positive Rate')