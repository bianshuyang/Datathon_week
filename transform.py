with open('rf_1951.TXT','r',encoding='utf-8') as f:
    a = f.readlines()
grand_index = 0
while grand_index<=364:
    pro = a[grand_index*34]
    pro = pro.replace('  ',' ').split(' ')
    title ='.'.join(pro[0:3])
    with open(title+'.csv','a',encoding='utf-8') as f:
        f.write(','+','.join(pro[3:]))
    lst_no = grand_index*34+1
    while lst_no<=grand_index*34+33:
        sample = a[lst_no].replace('\n','')
        sample = sample.split(' ')
        index = 0
        yangben = []
        while index<=len(sample)-1:
            if sample[index]!='':
                yangben.append(sample[index])
            index +=1
    #########
        index = 0
        sample = []
        while index<=len(yangben)-1:
            if yangben[index]!='-99.9':
                sample.append(yangben[index])
            else:
                sample.append('')
            index +=1
        lst_no +=1
        with open(title+'.csv','a',encoding='utf-8') as f:
            f.write(','.join(sample)+'\n')
    grand_index +=1
