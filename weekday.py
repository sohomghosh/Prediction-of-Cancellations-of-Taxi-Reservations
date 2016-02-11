fp=open("new4.csv",'r')
fp1=open("day.csv",'w')
fp.readline()
while True:
    line=fp.readline()
    if not line:
        break
    tk=line.split(',')
    if str(tk[10])!="NULL":
        fp1.write(str(tk[10])+"@"+str(tk[12]))
fp.close()
fp.close()