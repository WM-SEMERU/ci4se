def plot_counts(df, theme):
    dates, counts = df['date-observation'], df[theme + '_count']
    fig, ax = plt.subplots()
    ax.set_ylabel('{} pixel counts'.format(' '.join(theme.split('_'))))
    ax.set_xlabel('observation date')
    ax.plot(dates, counts, '.')
    fig.autofmt_xdate()
    plt.show()