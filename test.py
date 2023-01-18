f=open("bioinfoQ.txt").readlines()
for i in range(10):
    q,a=f[i].split(",")
    Q=open("test_"+str(i+1)+".txt","w").write(q+"\n")
    A=open("ans_"+str(i+1)+".txt","w").write(a)

    