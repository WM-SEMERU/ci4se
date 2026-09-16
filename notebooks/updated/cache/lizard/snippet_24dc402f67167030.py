def _runPopUp(workbench, popUp):
    workbench.display(popUp)
    d = popUp.notifyCompleted()
    d.addCallback(_popUpCompleted, workbench)
    return d