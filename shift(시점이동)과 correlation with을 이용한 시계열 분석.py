def correlations_mean(station,df_week_people_temp,df_week_dust_temp):
    answer=[]
    for i in station:
        #데이터를 station별로 나누는 작업
        df_week_people_station=df_week_people_temp[df_week_people['지점명']==i]
        df_week_dust_station=df_week_dust_temp[df_week_dust_temp['지점명']==i]
        df_week_dust_station.drop(labels={'호선','지점명','Date'},axis=1,inplace=True)
        df_week_people_station.drop(labels={'호선','지점명','Date','day'},axis=1,inplace=True)
        #일평균으로 보는 법
        df_week_people_station=df_week_people_station.mean()
        df_week_dust_station=df_week_dust_station.mean()
        df_week_dust_station=pd.DataFrame(df_week_dust_station)
        df_week_people_station=pd.DataFrame(df_week_people_station)
        #shifting 하는 작업
        shifted_df_week_dust=df_week_dust_station.shift(periods=-2,axis=0)
        shifted_df_week_dust=shifted_df_week_dust.iloc[:-2]
        df_week_people_station=df_week_people_station.iloc[:-2]
        df_week_people_station.reset_index(drop=True,inplace=True)
        #shifted_df_week_dust.reset_index(drop=True,inplace=True)
        df_week_dust_station.reset_index(drop=True,inplace=True)
        #print(shifted_df_week_dust)
        #corrs=shifted_df_week_dust.corrwith(df_week_people_station,axis=1)
        corrs=df_week_dust_station.corrwith(df_week_people_station)
        answer.append(sum(corrs)/len(corrs))
    return answer
station=df_week_dust['지점명'].unique()
answer=correlations_mean(station,df_week_people,df_week_dust)
answer