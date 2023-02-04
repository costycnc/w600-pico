W600-pico upload files over ftp in windows command prompt

Open online serial port monitor https://bipes.net.br/aroca/web-serial-terminal/ or another serial port monitor

Connect w600-pico with pc over usb cable.

Select 115200 speed and click connect.

Select port and click connect.

In serial terminal write 

    import easyw600

and hit Enter (send)

    easyw600.createap(ssid="W600_softAP")
    
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
