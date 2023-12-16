# import time
# from tkinter import *
#
# root = Tk()
# root.resizable(FALSE, FALSE)
# root.title("JAM GW KEREN")
#
# def waktu():
#     kontrol_waktu = time.strftime("%H:%M:%S")
#     label.config(text=kontrol_waktu)
#     label.after(200, waktu)
#
# label = Label(root, bg="black", fg="red", font="normal 100 bold")
# label.pack()
# waktu()
# root.mainloop()



import os
f = open("file/saldo.txt")

isi = f.read()
saldo = int(isi)
saldo = saldo - 200000
print(saldo)
f.close()

os.remove("filr/saldo.txt")
f = open("file/saldo.txt","a")
f.write(str(saldo))
f.close()



















