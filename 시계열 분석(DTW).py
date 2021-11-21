from pyts.metrics import dtw, itakura_parallelogram, sakoe_chiba_band
dtw_classic, cost = dtw(df_week_people.mean(), df_week_dust.mean(), dist='square',method='classic', return_path=True)
matrix_classic = np.zeros((df_week_people.mean().size, df_week_dust.mean().size))
matrix_classic[tuple(cost)] = 1.
plt.pcolor(df_week_people_Scaler.mean(), df_week_dust_Scaler.mean(), matrix_classic.T,
           edgecolors='k', cmap='Greys')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title("{0}\nDTW(x, y) = {1:.20f}".format('sakoechiba', dtw_classic),
          fontsize=14)