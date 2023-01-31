home page --> https://www.wemos.cc/en/latest/tutorials/w600/get_started_with_micropython_w600.html

ch340 driver -->  https://www.wemos.cc/en/latest/ch340_driver.html

pyton -->  https://www.python.org/downloads/

           pip install w600tool
           
micropython firmware http://www.winnermicro.com/upload/1/editor/1568709203932.zip 

          w600tool.py -p PORT_NAME -u FIRMWARE.fls

w600tool.py github --> https://github.com/vshymanskyy/w600tool

------------------------------  W600TOOL.EXE ------------------------------------------------

w600tool.exe github --> https://github.com/vshymanskyy/w600tool/releases/tag/0.1

download direct --> w600tool.exe  https://github.com/vshymanskyy/w600tool/releases/download/0.1/w600tool.exe

       C:\.....\w600tool.exe -u "C:\.....\firmware.fls" 
       the port is detected automatically
       
If main.py is in infinity loop add -e to renew flash default

      C:\....\w600tool.exe -e -u "C:\......\firmware.fls" 

