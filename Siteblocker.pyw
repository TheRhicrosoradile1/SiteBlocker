import time
from datetime import datetime as dt
start_t=input("Enter time of starting your work in whole number in 24 hour format\n e.g- 8 for 8am .\n 14 for 2pm \n and don't bullshit me with decimal value , i will fry your PC if you do that\n")
end_t=input("\nEnter time your work shift ends\n ")
test_path="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","m.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,int(start_t))<dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,int(end_t)):
        print("work now no facebook")
        time.sleep(15)
        with open(host_path,'r+') as file:
            content=file.read()
            
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write("\n" + redirect +" "+ site + "\n")
    else :
        print("Go play fat ass")
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any (sites in line for sites in website_list):
                    file.write(line)
                else:
                    pass
                    
        
        time.sleep(15)
