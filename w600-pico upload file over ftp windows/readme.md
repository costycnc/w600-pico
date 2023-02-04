W600-pico upload files over ftp in windows command prompt

Open online serial port monitor https://bipes.net.br/aroca/web-serial-terminal/ or another serial port monitor

Connect w600-pico with pc over usb cable.
[<img src="">](https://www.youtube.com/watch?v=bhKmkqbpgdc)
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

and hit Enter (send)

         easyw600.createap(ssid="W600_softAP")
    
and hit enter (send)

The response will be 
                                                                                                            
   softap working, ip is 192.168.43.1   

Now create ftp server

    import w600
    
and hit enter   

    w600.run_ftpserver(port=21,username="user",password="12345678")
    
and hit enter  

The response will be
                                                                                                            
      softap working, ip is 192.168.43.1
      
Now you have an access point ip 192.148.43.1 where working a ftp server on port 21 

Now need to prepare a folder where put and download files from or on w600-pico
     
Open any folder   (for example my documents) and write in address bar -->  cmd  

Will opened a dos cmd windows with path in this folder

write :

    ftp 192.168.43.1
    
the system will response with    

       Connesso a 192.168.43.1
       220-= welcome on W600 FTP server =-
       220
       502 Not Implemented.
       Utente (192.168.43.1:(none)):
       
the server request user name ... so write  -->  user       and hit enter

after server request password ... so write  --> 12345678   and hit enter

if all is ok will receive

       Utente (192.168.1.4:(none)): user
       331 Password required for user
       Password:
       230 User logged in
       ftp>

Now you can use ftp commands to download boot.py and main.py and write lines of code inside

So ... if write in console --> get main.py  the file main.py will be downloaded in current folderand file will 

Open main.py with notepad++ or another text editor and write some lines and save

From console write --> put main.py   and file will be uploaded to w600.pico

push reset button on w600-pico board or unplug and plug usb ... and program from main.py will be executed!



the most important ftp commands:

         dir --> list all files and folder from w600-pico
         put file --> upload file from pc local directory to w600-pico
         get file --->	Get file from the w600-pico to pc local directory
         bye	--> Exits from FTP.

All ftp commands here https://www.serv-u.com/ftp-server-windows/commands (i dont know if all commands is implemented!) 
