for i in station:
    tmp=df[df['Wind']]
    tmp.reset_index(drop=True,inplace=True)
    res = seasonal_decompose(tmp,model='additive', period=306)
    ax=res.plot()
    plt.show()