# w600-pico

        Create access point
        import easyw600
        easyw600.createap(ssid="W600_softAP")
        
with mu editor https://github.com/mu-editor/mu/releases/tag/1.1.0-alpha.2
this did about alpha.2 ... i not understand how appear w600 in listing ... i download but not appear ... need to study this topic https://forum.micropython.org/viewtopic.php?t=8503

also a good tutorial https://www.sigmdel.ca/michel/ha/w600/first_look_w600_en.html

vshymanskyy  Firmware upload tool for Winner Micro W600 & W601 WiFi  https://github.com/vshymanskyy/w600tool


https://docs.micropython.org/en/v1.8.2/esp8266/esp8266/tutorial/filesystem.html

        >>> import os
        >>> os.listdir()
        ['sys', 'lib', 'cert', 'boot.py', 'main.py', 'easyw600.py']
        
        
        write:
        >>> f = open('data.txt', 'w')
        >>> f.write('some data')
        9 
        >>> f.close()
        
        
        append:
        >>> f = open('data.txt', 'a')
        >>> f.write('some data')
        9 
        >>> f.close()
        
        --------------------------------------------------
        >>> f=open('main.py','w')
        >>> f.write('print("Costycnc foam cutter")')
        13
        >>> f.close()
        >>> f=open('main.py')
        >>> f.read()
        'print("aaaa")'
         >>> 
         
         RESET
    __            __
    \ \    /\    / /
     \ \  /  \  / /
      \ \/ /\ \/ / 
       \  /  \  /
       / /\  / /\ 
      / /\ \/ /\ \ 
     / /  \  /  \ \ 
    /_/    \/    \_\ 



    WinnerMicro W600
    Costycnc foam cutter <------
    MicroPython v1.10-282-g6a9b3cb-dirty on 2019-09-17; WinnerMicro module with W600
    Type "help()" for more information.
    
        -----------------------------------------------------------------
        

