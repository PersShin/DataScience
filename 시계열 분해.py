#만약 station안에 원하는 값이 없다면 try except를 사용해서 오류를 파해쳐보자!
import matplotlib.pyplot as plt
for i in station:
    try:
        tmp=df[df['Wind']==i]
        tmp.reset_index(drop=True,inplace=True)
        res = seasonal_decompose(tmp,model='additive', period=306)
        ax=res.plot()
        plt.show()
    except:
        print(end='')