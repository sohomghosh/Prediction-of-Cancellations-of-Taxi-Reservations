import datetime
import calendar
fp=open("new1.csv",'r')
fp1=open("new2.csv",'w')
i=0
fp.readline()
fp1.write("vehicle_model_id,travel_type_id,from_area_id,from_time,booking_created_time,time_difference(mins),from_lat,from_long,to_lat,to_long,day,distance,Car_Cancellation\n")
while True:
    line=fp.readline()
    if not line:
        break
    tk=line.split(',')
    a=tk[3]
    month, day, year = map(int, a.split('/'))
    date1 = datetime.date(year, month, day)
    #zz= calendar.day_name[date1.weekday()]
    #print zz
    da=date1.weekday()+1
    #i=i+1
    fp1.write(str(tk[0])+","+str(tk[1])+","+str(tk[2])+","+str(tk[4])+","+str(tk[5])+","+str(tk[6])+","+str(tk[7])+","+str(tk[8])+","+str(tk[9])+","+str(tk[10])+","+str(da)+","+str(tk[12])+","+str(tk[13]));
    #if i==1000:
     #   break
fp.close()
fp1.close()