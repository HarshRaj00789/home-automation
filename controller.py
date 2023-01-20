import pyfirmata

comport = 'COM6'

board =  pyfirmata.Arduino(comport)

digitalpin_1=board.get_pin('d:2:o')
digitalpin_2=board.get_pin('d:3:o')
digitalpin_3=board.get_pin('d:4:o')
digitalpin_4=board.get_pin('d:5:o')

def led(total):
    if total==0:
        digitalpin_1.write(0)
        digitalpin_2.write(0)
        digitalpin_3.write(0)
        digitalpin_4.write(0)
    elif total==1:
        digitalpin_1.write(1)
        digitalpin_2.write(0)
        digitalpin_3.write(0)
        digitalpin_4.write(0) 
    elif total==2:
        digitalpin_1.write(0)
        digitalpin_2.write(1)
        digitalpin_3.write(0)
        digitalpin_4.write(0)
    elif total==3:
        digitalpin_1.write(0)
        digitalpin_2.write(0)
        digitalpin_3.write(1)
        digitalpin_4.write(0)
    elif total==4:
        digitalpin_1.write(0)
        digitalpin_2.write(0)
        digitalpin_3.write(0)
        digitalpin_4.write(1)
        
  





        

