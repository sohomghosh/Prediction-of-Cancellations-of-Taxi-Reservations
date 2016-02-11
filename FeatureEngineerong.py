fp=open("new2.csv",'r')
fp1=open("new3.csv",'w')
i=0
fp.readline()
fp1.write("vehicle_model_id,travel_type_id,from_area_id,from_time,booking_created_time,time_difference(mins),from_lat,from_long,to_lat,to_long,day,distance,Car_Cancellation\n")
while True:
    line=fp.readline()
    if not line:
        break
    tk=line.split(',')
    a=tk[3]
    aa=a.split(':')
    aaa=int(aa[0])*60+int(aa[1])
    b=tk[4]
    bb=b.split(':')
    bbb=int(bb[0])*60+int(bb[1])
    fp1.write(str(tk[0])+","+str(tk[1])+","+str(tk[2])+","+str(aaa)+","+str(bbb)+","+str(tk[5])+","+str(tk[6])+","+str(tk[7])+","+str(tk[8])+","+str(tk[9])+","+str(tk[10])+","+str(tk[11])+","+str(tk[12]));
fp.close()
fp1.close()