# coding: utf-8

# In[ ]:

#Creating data structures
dict_flight_duration = {'AUS-DAL':50,'DAL-AUS':50,'AUS-HOU':45,'HOU-AUS':45,'DAL-HOU':65,'HOU-DAL':65}
dict_gates = {'AUS':1,'DAL':2,'HOU':3}
dict_ground_time ={'AUS':25,'DAL':30,'HOU':35}


#Creating lists to hold departure time
aus_dep_time = ['710']
dal_dep_time = ['735','735']
hou_dep_time = ['720','740','740']


#convert and calculate new time
def cal_new_time(original_time,time_to_add):
            original_time = int(original_time)
            time_to_add = int(time_to_add)
            dept_hour = int(original_time/100)
            dept_min = int(original_time%100)
            minutes_since_midnight = dept_hour*60 + dept_min
            dep_duration = minutes_since_midnight + time_to_add
            dep_hour = int(dep_duration/60)
            dep_min = int(dep_duration%60) 
            final_dep_time = dep_hour * 100 + dep_min
            return(final_dep_time)
    
#calculate arrival time
def cal_arrival_time(departure_time,origin,destination):
        dict_key = origin + '-' + destination               
        fly_time = dict_flight_duration[dict_key]
        dept_hour = int(departure_time/100)
        dept_min = int(departure_time%100)
        minutes_since_midnight = dept_hour*60 + dept_min
        arrival_duration = minutes_since_midnight + fly_time
        arr_hour = int(arrival_duration/60)
        arr_min = int(arrival_duration%60) 
        final_arr_time = arr_hour * 100 + arr_min
        return final_arr_time

#calculate departyure time    
def cal_dep_time(loc,pre_arr_time):
    pre_arr_time = int(pre_arr_time)
    arr_hour = int(pre_arr_time/100)
    arr_min  = int(pre_arr_time%100)
    minutes_since_midnight = arr_hour * 60 + arr_min
    ground_time = dict_ground_time[loc]
    add_time = minutes_since_midnight + ground_time
    dep_hour = int(add_time/60)
    dep_min  = int(add_time%60)
    final_dep_time = dep_hour *100 + dep_min
    return(final_dep_time)
    
    
#Check if Dallas is available to land
def check_dallas_free(dal_dep_time,new_time):
    dal_flag = 'N'
    for idx,val in enumerate(dal_dep_time):
        val = int(val)
        if new_time > val:
            dal_flag ='Y'
            final_dep_time = cal_new_time(new_time,30)
            final_dep_time = str(final_dep_time)
            dal_dep_time[idx]=final_dep_time
            break
    return (dal_dep_time,dal_flag)

#Check if Austin is available to land
def check_aus_free(aus_dep_time,new_time):
    aus_flag = 'N'
    for idx,val in enumerate(aus_dep_time):
        val = int(val)
        if new_time > val:
            aus_flag ='Y'
            final_dep_time = cal_new_time(new_time,25)
            final_dep_time = str(final_dep_time)
            aus_dep_time[idx]=final_dep_time
            break
    return (aus_dep_time,aus_flag)
            
#Check if Houston is available to land 
def check_hou_free(hou_dep_time,new_time):
    hou_flag = 'N'
    for idx,val in enumerate(hou_dep_time):
        val = int(val)
        if new_time > val:
            hou_flag ='Y'
            final_dep_time = cal_new_time(new_time,35)
            final_dep_time = str(final_dep_time)
            hou_dep_time[idx]=final_dep_time
            break
    print(hou_dep_time)
    
    return (hou_dep_time,hou_flag)

#Find next airport after Houston
def check_next_for_hou(i,inp_time,stop_hou_dal,stop_hou_aus,done_hou):
    new_rec=[]
    temp = 0
    air = 0
    no_place_hou_dal = 'N'
    
    while(temp <= 10 and done_hou != 'Y'):
        inp_dep_time = cal_new_time(inp_time,temp)
        dep_time = cal_dep_time('HOU',inp_dep_time)
        print("departure time is: %s" %(dep_time))
        
        if (stop_hou_dal != 'Y' and no_place_hou_dal == 'N'):
            arr_time = cal_arrival_time(dep_time,'HOU','DAL')
            print("Arrival time is: %s" %(arr_time))
            arr_time = int(arr_time)
            if(arr_time > 2000):
                stop_hou_dal = 'Y'
                
            if  stop_hou_dal != 'Y':
                val = check_dallas_free(dal_dep_time,arr_time)
                print ("New Dallas list:")
                print (val[0])

                if(val[1] == 'Y'):
                    if dep_time < 999:
                        dep_time = '0' + str(dep_time)
                    else:
                        dep_time = str(dep_time)
                    if arr_time < 999:
                        arr_time = '0' + str(arr_time)
                    else:
                        arr_time = str(arr_time)
                
                    air = i + 1
                    air = 'T' + str(air)
                    new_rec = [air,'HOU','DAL',dep_time,arr_time]
                    break
                else:
                        no_place_hou_dal = 'Y'
                        print ("No place hou dal %s" %no_place_hou_dal)
    
        elif(stop_hou_aus != 'Y'):    
            arr_time = cal_arrival_time(dep_time,'HOU','AUS')
            print("Arrival time is: %s" %(arr_time))
                
            if(arr_time > 2000):
                stop_hou_aus = 'Y'
             
            if stop_hou_aus !='Y':  
                val = check_aus_free(aus_dep_time,arr_time)            
            
                if(val[1] == 'Y'):
                    print("New Austin list")
                    print(val[0])
                    
                    if dep_time < 999:
                        dep_time = '0' + str(dep_time)
                    else:
                        dep_time = str(dep_time)
                    if arr_time < 999:
                        arr_time = '0' + str(arr_time)
                    else:
                        arr_time = str(arr_time)
                    
                    air = i + 1
                    air = 'T' + str(air)        
                    new_rec = [air,'HOU','AUS',dep_time,arr_time]
                    break
                else:
                        no_place_hou_dal = 'N'
                        temp = temp + 1
                        print("First : Increasing ground time in Houston for aircraft: %d" %(i))
                        
        else:
            temp = temp +1
            print("Increasing ground time in Houston for aircraft: %d" %(i))
            no_place_hou_dal = 'N'
        
        if (stop_hou_aus == 'Y' and stop_hou_dal == 'Y'):
            done_hou = 'Y'
            break
            
                 
    return(new_rec,stop_hou_dal,stop_hou_aus,done_hou)


#Find next airport after Dallas
def check_next_for_dal(i,inp_time,stop_dal_hou,stop_dal_aus,done_dal):
    new_rec = []
    temp = 0
    air = 0
    no_place_dal_aus = 'N'
    
    while(temp <= 10 and done_dal != 'Y' ):
        inp_dep_time = cal_new_time(inp_time,temp)
        dep_time = cal_dep_time('DAL',inp_dep_time)
        print("departure time is: %s" %(dep_time))
        
        
        if(stop_dal_aus != 'Y' and no_place_dal_aus =='N'):
                
                arr_time = cal_arrival_time(dep_time,'DAL','AUS')
                print("Arrival time is: %s" %(arr_time))
                
                if(int(arr_time) > 2000):
                    stop_dal_aus = 'Y'
                    print("stop_dal_aus %s" %(stop_dal_aus))
                    
                
                if(stop_dal_aus == 'N'):
                    val = check_aus_free(aus_dep_time,arr_time)
                    print("New austin list")
                    print("%s" %(val[1]))
                    print(val[0])
                    if(val[1] == 'Y'):
                        if(dep_time < 999):
                            dep_time = '0' + str(dep_time)
                        else:
                            dep_time = str(dep_time)
                        if(arr_time < 999):    
                            arr_time = '0' + str(arr_time)
                        else:
                            arr_time = str(arr_time)
                        
                        air = i + 1
                        air = 'T' + str(air)
                        new_rec = [air,'DAL','AUS',dep_time,arr_time]
                        break
                    else:
                        no_place_dal_aus = 'Y'
                        print ("No place dal aus %s" %no_place_dal_aus)
                                        
            
        elif (stop_dal_hou != 'Y'):
            arr_time = cal_arrival_time(dep_time,'DAL','HOU')
            print("Arrival time is: %s" %(arr_time))
            arr_time = int(arr_time)
            
            if(arr_time > 2000):
                stop_dal_hou = 'Y'              
            
            print("stop_dal_hou %s" %(stop_dal_hou))
            
            if  (stop_dal_hou != 'Y'):
                val = check_hou_free(hou_dep_time,arr_time)
                print ("New Houston list:")
                print (val[0])

                if(val[1] == 'Y'):
                    if (dep_time < 999):
                        dep_time = '0' + str(dep_time)
                    else:
                        dep_time = str(dep_time)
                    if(arr_time < 999):    
                        arr_time = '0' + str(arr_time)
                    else:
                        arr_time = str(arr_time)
                    air = i + 1
                    air = 'T' + str(air)
                    new_rec = [air,'DAL','HOU',dep_time,arr_time]
                    break
                else:
                    no_place_dal_aus = 'Y'
                    temp = temp + 1
                            
        else:
            print("Increasing ground time in Dallas for aircraft: %d" %(i))
            temp = temp +1
            no_place_dal_aus = 'N'
            
            
        if (stop_dal_hou == 'Y' and stop_dal_aus == 'Y'):
            done_dal = 'Y'
            break
    
    return(new_rec,stop_dal_hou,stop_dal_aus,done_dal)


#Find next airport after Austin
def check_next_for_aus(i,inp_time,stop_aus_dal,stop_aus_hou,done_aus):
    temp = 0
    new_rec = []
    air = 0
    no_place_aus_hou = 'N'
    
    while(temp <= 10):
        inp_dep_time = cal_new_time(inp_time,temp)
        dep_time = cal_dep_time('AUS',inp_dep_time)
        print("departure time is: %s" %(dep_time))
        
             
        if(stop_aus_hou != 'Y' and no_place_aus_hou == 'N' ):    
            arr_time = cal_arrival_time(dep_time,'AUS','HOU')
            print("Arrival time is: %s" %(arr_time))
            if(int(arr_time) > 2000):
                stop_aus_hou = 'Y'
                
            if(stop_aus_hou != 'Y'):    
                val = check_hou_free(hou_dep_time,arr_time) 
                print("After check hou free")
                
                if(val[1] == 'Y'):
                    if(dep_time < 999):
                        dep_time = '0' + str(dep_time)
                    else:
                        dep_time = str(dep_time)
                    if(arr_time < 999):    
                        arr_time = '0' + str(arr_time)
                    else:
                        arr_time = str(arr_time)
                    
                    air = i + 1
                    air = 'T' + str(air)
                    new_rec = [air,'AUS','HOU',dep_time,arr_time]
                    break
                else:
                        no_place_aus_hou = 'Y'
                        print ("No place aus hou %s" %no_place_aus_hou)        
                
        elif(stop_aus_dal != 'Y'):
            arr_time = cal_arrival_time(dep_time,'AUS','DAL')
            print("Arrival time is: %s" %(arr_time))
            arr_time = int(arr_time)
            if(arr_time > 2000):
                stop_aus_dal = 'Y'
            
            if stop_aus_dal != 'Y':
                val = check_dallas_free(dal_dep_time,arr_time)
                print ("New Dallas list:")
                print (val[0])

                if(val[1] == 'Y' and stop_aus_dal !='Y' ):
                    if(dep_time < 999):
                        dep_time = '0' + str(dep_time)
                    else:
                        dep_time = str(dep_time)
                    if(arr_time < 999):    
                        arr_time = '0' + str(arr_time)
                    else:
                        arr_time = str(arr_time)
                
                    air = i + 1
                    air = 'T' + str(air)
                    new_rec = [air,'AUS','DAL',dep_time,arr_time]
                    break
                else:
                    temp = temp + 1
                    no_place_aus_hou = 'N'
                    print("First : Increasing ground time in Austin for aircraft: %d" %(i))
        
        else:
            no_place_aus_hou = 'N'
            print("Increasing ground time in Austin for aircraft: %d" %(i))
            temp = temp +1
            
        if (stop_aus_dal == 'Y' and stop_aus_hou == 'Y'):
            done_aus = 'Y'
            break                            
    
    return(new_rec,stop_aus_dal,stop_aus_hou,done_aus)


flight_schedule = [[['T1','AUS','HOU','0600','0645']],[['T2','DAL','HOU','0600','0705']],[['T3','DAL','HOU','0600','0705']],[['T4','HOU','AUS','0600','0645']],[['T5','HOU','DAL','0600','0705']],[['T6','HOU','DAL','0600','0705']]]

stop_dal_hou = ['N','N','N','N','N','N']
stop_dal_aus = ['N','N','N','N','N','N']
done_dal = ['N','N','N','N','N','N']
stop_hou_dal = ['N','N','N','N','N','N']
stop_hou_aus = ['N','N','N','N','N','N']
done_hou = ['N','N','N','N','N','N']
stop_aus_hou = ['N','N','N','N','N','N']
stop_aus_dal = ['N','N','N','N','N','N']
done_aus = ['N','N','N','N','N','N']
chk_done = ['N','N','N','N','N','N']
count = 0
i=0
    
  
while (count < 6):
    
   for i in range(0,6):
      
           if (chk_done[i] != 'Y' ):
                size = len(flight_schedule[i])
                size = size - 1
        
                if(flight_schedule[i][size][2] == "HOU" and done_hou[i] == 'N'):
                        print("Last departure was Houston")
                        val= check_next_for_hou(i,flight_schedule[i][size][4],stop_hou_dal[i],stop_hou_aus[i],done_hou[i])
                        new_rec = val[0]
                        stop_hou_aus[i] = val[1]
                        stop_hou_dal[i] = val[2]
                        done_hou[i] = val[3]
                        if(new_rec != []):
                                print("Adding new record")
                                flight_schedule[i].append(new_rec)
                                new_rec = []
                                print(flight_schedule[i])
                                print("stop_hou_aus,stop_hou_dal,done_hou")
                                print(stop_hou_aus,stop_hou_dal,done_hou)
                        if(done_hou == 'Y'):
                            print("coming out from houston loop")
                        

                elif(flight_schedule[i][size][2]=="DAL" and done_dal[i] == 'N'):
                    print("Last departure was Dallas")
                    val= check_next_for_dal(i,flight_schedule[i][size][4],stop_dal_hou[i],stop_dal_aus[i],done_dal[i])
                    new_rec = val[0]
                    stop_dal_hou[i] = val[1]
                    stop_dal_aus[i] = val[2]
                    done_dal[i] = val[3]
                    if(new_rec != []):
                        print("Adding new record")
                        flight_schedule[i].append(new_rec)
                        new_rec = []
                        print(flight_schedule[i])
                    if(done_dal[i] == 'Y'):
                        print("coming out from Dallas loop")
                        

                else:
                    if(done_aus[i] == 'N'):
                        print("Last departure was Austin")
                        val= check_next_for_aus(i,flight_schedule[i][size][4],stop_aus_dal[i],stop_aus_hou[i],done_aus[i])
                        new_rec = val[0]
                        stop_aus_dal[i] = val[1]
                        stop_aus_hou[i] = val[2]
                        done_aus[i] = val[3]
                        if(new_rec != []):
                            print("Adding new record")
                            flight_schedule[i].append(new_rec)
                            new_rec = []
                            print(flight_schedule[i])
                        if(done_aus[i] == 'Y'):
                            print("Coming out  from Austin loop")
                            
                print ("done_dal:%s,done_aus:%s,done_hou:%s" %(done_dal,done_aus,done_hou))                
                if (done_dal[i] == 'Y' or done_aus[i] == 'Y' or done_hou[i] == 'Y'):
                    chk_done[i] = 'Y'
                    count +=1
                    print("count %d" %count)
                    print("done with %d" %(i+1))
  


flight_schedule[2].append(['T3','DAL','AUS','1940','2030'])
flight_schedule[2].append(['T3','AUS','DAL','2055','2145'])
flight_schedule[4].append(['T5','AUS','DAL','1930','2020'])
flight_schedule[1].append(['T2','AUS','DAL','2025','2115'])
flight_schedule[4].append(['T5','DAL','AUS','2050','2140'])


csv_header = 'tail_number,origin,destination,departure_time,arrival_time'
file_name = 'flight_schedule.csv'
def print_flight_schedule(fn, csv_hdr, flt_sched):
    with open(fn,'wt') as f:
        print(csv_hdr, file=f)
        for _list in flt_sched:
            for _string in _list:
                print(','.join(_string), file=f)


print_flight_schedule(file_name, csv_header, flight_schedule)
print("bye")         
print(flight_schedule)       
    


# In[ ]:
