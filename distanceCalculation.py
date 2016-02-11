import math
fp=open("new3.csv",'r')
fp1=open("new4.csv",'w')
i=0
fp.readline()
fp1.write("vehicle_model_id,travel_type_id,from_area_id,from_time,booking_created_time,time_difference(mins),from_lat,from_long,to_lat,to_long,day,distance(km),Car_Cancellation\n")
while True:
    line=fp.readline()
    if not line:
        break
    tk=line.split(',')
    f_lat=float(tk[6])
    f_lon=float(tk[7])
    t_lat=float(tk[8])
    t_lon=float(tk[9])
    dlon = t_lon - f_lon
    dlat = t_lat - f_lat
    a = (math.sin(dlat/2))*(math.sin(dlat/2)) + math.cos(f_lat) * math.cos(t_lat) * (math.sin(dlon/2)*math.sin(dlon/2))
    c = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a) )
    d = 6371 * c
    fp1.write(str(tk[0])+","+str(tk[1])+","+str(tk[2])+","+str(tk[3])+","+str(tk[4])+","+str(tk[5])+","+str(tk[6])+","+str(tk[7])+","+str(tk[8])+","+str(tk[9])+","+str(tk[10])+","+str(d)+","+str(tk[12]));
fp.close()
fp1.close()