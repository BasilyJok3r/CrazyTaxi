from ast import Try
import time
import serial

serialComm = 0
is_inited = False


# start by using this function
def init_comm(port="COM3"):
    global serialComm
    global is_inited
    try:
        serialComm = serial.Serial("COM3", 9600, timeout=1)
        time.sleep(2)
        is_inited = True
    except:
        print("couldn't init")
        is_inited = False

# this would be used to communicate with the car   
# msgs = { 'f' , 'b' , 'l' , 'r' }
def car_go(msg, show_response = False,show_prints = False):
    global serialComm
    global is_inited

    if not is_inited:
        print("init communication!")
        return
    msg = msg.strip()
    serialComm.write(msg.encode())
    time.sleep(0.1)
    if show_response:
        print(serialComm.readline().decode('ascii'))

    if show_prints:
        if msg == "r":
            print("right->")
        elif msg == "l":
            print("<-left")
        if msg == "f":
            print("forward^")
        elif msg == "b":
            print("backward|")



# excute this at end of the program
def end_comm():
    global serialComm
    global is_inited
    if not is_inited:
        print("init communication!")
        return
    serialComm.close()
    is_inited = False




# def test__():
#     init_comm()
#     car_go("f")
#     end_comm()


# test__()