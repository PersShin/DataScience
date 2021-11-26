#만약에 열이름이 다른 경우 corrwith이 nan값을 반환하게 된다.
#예를 들어, 6과 '6'은 다른 경우로 인식을 한다. 따라서, 6을 str형태로 바꾸든, '6'을 int형태로 바꿔야한다.
#밑 예시는  int->str이다.
import pandas as pd
season_out_dust=pd.DataFrame(season_out_dust)
season_out_dust.rename(columns= lambda x:str(x), inplace=True)
season_in_dust=pd.DataFrame(season_in_dust)

corr_out_in=season_out_dust.corrwith(season_in_dust,axis=1)