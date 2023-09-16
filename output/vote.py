
def add_data(datalst,dct):
    for datai in range(len(datalst)):
        if datalst[datai] not in dct:
            dct[datalst[datai]]=1
        else:
            dct[datalst[datai]]+=1
    return dct


def compare(data1,data2):
    cnt=0
    for i in range(len(data1)):
        if data1[i]==data2[i]:
            cnt+=1
    print(round(cnt/len(data1)*100,2))


def vote():

    f1=open("prompt-augmented-A_output.txt","r",encoding="utf8")
    data1=f1.readlines()

    f2=open("prompt-augmented-B_output.txt","r",encoding="utf8")
    data2=f2.readlines()

    f3=open("retrieval-augmented_output.txt","r",encoding="utf8")
    data3=f3.readlines()


    gold=open("gold.txt","r",encoding="utf8").readlines()

    print("prompt-augmented-modelA:")
    compare(data1,gold)
    print("prompt-augmented-modelB:")
    compare(data2,gold)
    print("retrieval-augmented-model:")
    compare(data3,gold)

    cnt=0
    vote_ans=[]
    index=[]


    for i in range(len(data1)):
        dct={}
        datalst=[data1[i],data2[i],data3[i]]


        add_data(datalst,dct)


        max=0
        maxwu=dct[list(dct.keys())[0]]

        for j in dct:
            if dct[j]>max:
                max=dct[j]
                maxwu=j

        if maxwu==gold[i]:
            cnt+=1
            index.append(str(i)+"\n")
        vote_ans.append(maxwu)

    print("enfiner:")
    print(round(cnt/len(data1)*100,2))



vote()