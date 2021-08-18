import os
os.system ("clear")
try :
    import pyautogui
except ImportError :
    os.system ("pip install pyautogui")
    
while True :
   pyautogui.write ("Hi")
   pyautogui.press ("enter")
  
# Done :")
   
