import sys
import string
import numbers
from typing import ItemsView

def ask_for_input():
    floor,slots=int(input("Enter the floor to create the parking lot:")), int(input("Enter the slots(must be >=2) to create the parking lot:"))
    return floor,slots
    
def ask_for_typeno():
    vno,tvehic=input("Enter Vehicle no:Template-XX00XX0000: "),input("Enter type of Vehicle:B/C:")
    return tvehic, vno;

def ask_ticid():
    ticid,ttype=input("Enter ticid:"), input("Enter Vehicle type: BIKE/CAR?:")
    return ticid,ttype

def car_bike_allocate(floor,carslot,car1,bike1):
    if floor not in car1:
        car1[floor]=carslot
        bike1[floor]=2
        return car1,bike1
    car1[floor]+=carslot
    bike1[floor]=2
    return car1,bike1
    

def create_parkinglot(floor,slots):
    if floor not in floors:
        floors.append(floor)
        fslots[floor]=slots
    else:
        fslots[floor]+=slots
    return fslots

def show_available_slots():
    print("The available slots for Bike:{}\n".format(str(t_bikeslot)))
    print("The available slots for Cars:{}\n".format(str(t_carslot)))
    return
    
def create_ticid(tvehicle,vno,carbikeslot,tid_ids,t_slot):
    if len(tid_ids)==0:
        tic_tid=1
        t_slot-=1
    else:
        tic_tid=int(tid_ids[-1])+1
        t_slot-=1
    return tic_tid,t_slot

'''def unpark_vehicle(ticid, ttic_ids):
    tvno=ttic_ids[ticid]
    return tvno '''




i=0
floors=[]
carslot={}
bikeslot={}
fslots={}
tic_id={}
car={}
bike={}
tic_ids={}
t_carslot=0
t_bikeslot=0

while (True):
    inputu=int(input("What can code for you? Choose one of below option\n1. Create parking lot\n2. Park the Vehicle\n3. Unpark the vehicle\n4. show the avaible slots\n Any other option will exit:\n"))
    if inputu==1:
        floor,slots=ask_for_input()
        fslots1=create_parkinglot(floor,slots)
        fslots.update(fslots1)
        carsl=slots-2
        car1,bike1=car_bike_allocate(floor,carsl,carslot,bikeslot)
        carslot.update(car1)
        bikeslot.update(bike1)
        print("parking for {} floor created with {} slots,\n".format(str(floor),str(slots)))
        print("parking for cars are: {} and bikes are: {}\n".format(str(carslot[floor]),str(bikeslot[floor])))
        t_carslot+=carsl
        t_bikeslot+=2
        print("Total slots for car and bike respectively: {} and {}\n".format(str(t_carslot),str(t_bikeslot)))
    elif inputu==2:
        tvehicle,vno=ask_for_typeno()
        if tvehicle.upper()=="CAR":
            if len(carslot)<1 or len(car)>t_carslot:
                print("parking is full or not available for cars\n")
                continue
            tic_id,t_carslot=create_ticid(tvehicle,vno,carslot,list(tic_ids.values()),t_carslot)
            car[vno]=tic_id
            tic_ids[vno]=tic_id
        elif tvehicle.upper()=="BIKE":
            if len(bikeslot)<1 or len(bike)>t_bikeslot:
                print("parking is full or not available for bikes1\n")
                print(bike, len(bikeslot), t_bikeslot)
                continue
            tic_id,t_bikeslot=create_ticid(tvehicle,vno,bikeslot,list(tic_ids.values()),t_bikeslot)
            bike[vno]=tic_id
            tic_ids[vno]=tic_id
        else:
            print("Invalid type of Vehicle\n")
            continue
        print(tic_ids)
        print("Ticket ID for {} with {} is created. Tic_ID={}\n".format(str(tvehicle),str(vno),str(tic_id)))
    elif inputu==3:
        ticid,ttype=ask_ticid()
        temp1=list(tic_ids.values())
        print(temp1)
        if int(ticid) not in list(tic_ids.values()):
            print("Invalid Ticket ID or Ticket ID doesnt exist:\n")
            continue
        #vnum=unpark_vehicle(ticid,tic_ids)
        if ttype.upper()=="BIKE":
            for key,value in bike.items():
                if value==int(ticid):
                    bike.pop(key)
                    t_bikeslot+=1
                    tic_ids.pop(key)
                    print("the ticket ID: {} for bike number: {} has left the parking\n".format(ticid,key))
                    break  
        else:
            for key,value in car.items():
                if value==int(ticid):
                    car.pop(key)
                    tic_ids.pop(key)
                    t_carslot+=1
                    print("the ticket ID: {} for car number: {} has left the parking\n".format(ticid,key))
                    break

    elif inputu==4:
        show_available_slots()
    else:
        print("Invalid option")
        sys.exit()
