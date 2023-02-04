W600-pico upload files over ftp in windows command prompt

Open online serial port monitor https://bipes.net.br/aroca/web-serial-terminal/ or another serial port monitor

Connect w600-pico with pc over usb cable.

Select 115200 speed and click connect.

Select port and click connect.

Once coneccted will see in terminal response of w600-pico micropython

           \ \  /  \  / /                                                                                                                                   
            \ \/ /\ \/ /                                                                                                                                    
             \  /  \  /                                                                                                                                     
             / /\  / /\                                                                                                                                     
            / /\ \/ /\ \                                                                                                                                    
           / /  \  /  \ \                                                                                                                                   
          /_/    \/    \_\                                                                                                                                  
       Traceback (most recent call last):                                                                                                                    
        File "boot.py", line 1, in <module>                                                                                                                 
       NameError: name         '�� ' isn't defined                                                                                                                          Traceback (most recent call last):                                                                                                                    
       File "main.py", line 1, in <module>                                                                                                                 
       NameError: name '����������������������������������' isn't defined                                                                                    
       MicroPython v1.10-282-g6a9b3cb-dirty on 2019-09-17; WinnerMicro module with W600                                                                      
       Type "help()" for more information.  
       
Receive some errors because files boot.py   and main.py is empty    

Now you can send commands manually to w600-pico.

Here https://www.wemos.cc/en/latest/tutorials/w600/get_started_with_micropython_w600.html  some examples from official sites.

Next step is to set a access point and ftp server with only 4 lines of code !!!! after you cand send and receive files from w600-pico over ftp

Set access point to connect with w600-pico directly - no router!!! ( after you can write boot.py and main.py and send over ftp to connect to router)

In serial terminal write (create an AP access point -- local )

import easyw600
easyw600.createap(ssid="W600_softAP")

and hit Enter (send)


    
and hit enter (send)



The response will be 

     softap working, ip is 192.168.43.1
     
open any folder   (for example my documents) and write in address bar -->  cmd  

Will opened a dos cmd windows with path in this folder

write :

    ftp 192.168.1.43
    
the system will response with    


the most important ftp commands:

         dir --> list all files and folder from w600-pico
         put file --> upload file from pc local directory to w600-pico
         get file --->	Get file from the w600-pico to pc local directory
         bye	--> Exits from FTP.

All ftp commands here https://www.serv-u.com/ftp-server-windows/commands (i dont know if all commands is implemented!) 
