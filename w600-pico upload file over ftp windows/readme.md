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
