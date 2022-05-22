#처음에는 id에 따라 데이터를 뽑는다.
list_for_id=df['Arbitration_ID'].unique()
for i in list_for_id:
    print(i)
    temp=df[df['Arbitration_ID']==i]
    counter=temp['DLC'].unique()
    max_counter=max(counter)
    temp=temp.reset_index(drop=True)
    label=0#양성이 0
    label_sheet=[]
    id_sheet=[]
    #256개의 데이터-> 16*16-> 32*8
    for q in range(0,int(temp.shape[0]/32)):
        label=0
        n=0
        t_temp=[]
        #총 16개의 hex값은 string으로 len가 32이므로 32*16이다. 
        while len(t_temp)<512:
            #만약 전체 데이터의 크기보다 큰 경우 에러가 나 break
            if n+32*q>=len(temp):
                print(n+32*q,len(temp))
                break
                
            if len(t_temp)==0:
                t_temp=temp['Data'][n+32*q]
                
                if temp['Class'][n+32*q]=='Attack':
                    label=1
                    
            else:
                t_temp+=temp['Data'][n+32*q]
                
                if temp['Class'][n+32*q]=='Attack':
                    label=1 
                    
            t_temp=t_temp.replace(' ','')
            n+=1
        #만약 전체 데이터의 크기보다 큰 경우 에러가 나 break(pic을 만들수 없음)    
        if n+32*q>=len(temp):
            break
            
        #정확하게 안떨어지면 뒤에꺼 삭제
        if len(t_temp)>512:
            t_temp=t_temp[:512-len(t_temp)]
        
        newstring = bytearray.fromhex(t_temp)
        file = open('./train/bin/sample'+i+'_'+str(q)+'.bin', "wb")
        file.write(newstring)
        file.close()
        finer=making_pic(str(q),i)
        #csv파일 만들기 위해 필요한 값 list에 저장
        label_sheet.append(label)
        id_sheet.append(str(q))
    df_temp = pd.DataFrame((zip(id_sheet, label_sheet)), columns = ['ID', 'label'])
    df_temp.to_csv('./train/train_file_'+i+'.csv')