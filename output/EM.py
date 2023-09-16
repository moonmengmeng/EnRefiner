f1=open("enrefiner_output.txt","r",encoding="utf8")
data1=f1.readlines()
f2=open("gold.txt","r",encoding="utf8")
data2=f2.readlines()
cnt=0
for i in range(len(data1)):
    if data1[i]==data2[i]:
        cnt+=1

print("Number of successfully refinement:",cnt)
print("EM:",round(cnt/len(data1)*100,2))