def plot_ltc(LTC_CM, LTC_CT, LTC_WM, LTC_WT, e):
    leglist, init = [], 0
    if len(LTC_CM) > 2:
        if init == 0:
            plot_init(1, 5, 5)
        plt.plot(LTC_CT, LTC_CM, 'b')
        leglist.append('RT SIRM, measured while cooling')
        init = 1
    if len(LTC_WM) > 2:
        if init == 0:
            plot_init(1, 5, 5)
        plt.plot(LTC_WT, LTC_WM, 'r')
        leglist.append('RT SIRM, measured while warming')
    if init != 0:
        plt.legend(leglist, 'lower left')
        plt.xlabel('Temperature (K)')
        plt.ylabel('Magnetization (Am^2/kg)')
        if len(LTC_CM) > 2:
            plt.plot(LTC_CT, LTC_CM, 'bo')
        if len(LTC_WM) > 2:
            plt.plot(LTC_WT, LTC_WM, 'ro')
        plt.title(e)