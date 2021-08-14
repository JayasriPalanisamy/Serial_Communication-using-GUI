import serial
import tkinter as tk

serialPort = serial.Serial(port="COM10", baudrate=9600,
                           stopbits=serial.STOPBITS_ONE,
                           bytesize=8, timeout=2)
if not serialPort.isOpen():
    serialPort.open()
window = tk.Tk()
window.title("UART serial values")
window.geometry("300x250")
lbl_serial_value = tk.Label(text="Serial Value:")
lbl_serial_value.place(x=120, y=29)


def serial_value(label):
    def count():
        data = serialPort.readline()
        data1 = data[:-2].decode("utf-8")
        label.config(text=data1)
        window.after(2, count)
    count()


lbl_value = tk.Label(window, fg = "black")
lbl_value.pack()
serial_value(lbl_value)
button = tk.Button(window, text='Stop', width=25, command=window.destroy)
button.pack()
window.mainloop()
