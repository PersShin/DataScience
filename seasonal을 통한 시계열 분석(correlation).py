for i in station:
    df_week_p=df_week_people[df_week_people['지점명']==i]
    df_week_p.reset_index(drop=True,inplace=True)
    df_week_p=df_week_p.iloc[:,4:]
    df_week_p=df_week_p.mean()
    df_week_p=df_week_p.iloc[:-2]
    #
    df_week_d=df_week_dust[df_week_dust['지점명']==i]
    df_week_d=df_week_d.iloc[:,3:]
    df_week_d=df_week_d.shift(periods=-2,axis=1)
    df_week_d=df_week_d.mean()
    df_week_d=df_week_d.iloc[:-2]
    res = seasonal_decompose(df_week_p,model='additive', period=8)
    season_week_people.append(res.seasonal)
    res = seasonal_decompose(df_week_d,model='additive', period=8)
    season_week_dust.append(res.seasonal)   
season_week_people=pd.DataFrame(season_week_people)

def correlation_season(dust,people):
    temp=dust.corrwith(people,axis=1)
    return temp
corr_season=correlation_season(season_week_dust,season_week_people)