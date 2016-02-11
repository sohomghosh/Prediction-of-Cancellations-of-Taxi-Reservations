fp=open("new.csv",'r')
fp1=open("new1.csv",'w')
fp1.write("vehicle_model_id,travel_type_id,from_area_id,from_date_mm/dd/yyyy,from_time,from_day,booking_created_mm/dd/yyyy,booking_created_time,time_difference(mins),from_lat,from_long,to_lat,to_long,distance,Car_Cancellation\n")
fp.readline()
#i=0
print "hello"
while True:
    line=fp.readline()
    if not line:
        break
    tk=line.split(',')
    a=tk[3]
    aa=a.split(' ')
    aaa1=aa[0].split('/')
    aaa2=aa[1].split(':')
    ca=(int(aaa1[0])-1)*30*24*60+(int(aaa1[1])-1)*24*60 + int(aaa2[0])*60+int(aaa2[1])


    b=tk[4]
    bb=b.split(' ')
    bbb1=bb[0].split('/')
    bbb2=bb[1].split(':')
    cb=(int(bbb1[0])-1)*30*24*60+(int(bbb1[1])-1)*24*60 + int(bbb2[0])*60+int(bbb2[1])

    cc=ca-cb
    #print line
    #print cc
    #d=aa[0].split('/')
   # d=d[]
    fp1.write(str(tk[0])+","+str(tk[1])+","+str(tk[2])+","+str(aa[0])+","+str(aa[1])+","+"day"+","+str(bb[0])+","+str(bb[1])+","+str(cc)+","+str(tk[5])+","+str(tk[6])+","+str(tk[7])+","+str(tk[8])+","+","+str(tk[9]))
    #if i==14:
     #   break
    #i=i+1

fp.close()
fp1.close()