from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import serial


serial_port_para = {'port': 'COM10', 'baudrate': '9600'}

def serial_ports():
    ports = ['COM%s' % (i + 1) for i in range(256)]
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def set_serial_port():
    serial_port_para['port'] = com_b.currentText()

def set_baud_rate():
    serial_port_para['baudrate'] = com_b_1.currentText()

def dialog():
    mbox = QMessageBox()
    mbox.setWindowTitle("Serial Communication")
    mbox.setText("Serial Values")
    serialPort = serial.Serial(port=serial_port_para['port'], 
                           baudrate=int(serial_port_para['baudrate']),
                           stopbits=serial.STOPBITS_ONE,
                           bytesize=8, timeout=2)
    
    def count():
        data = serialPort.readline()
        data1 = data[:-2].decode("utf-8")
        mbox.setDetailedText(f"{data1}")
        QtCore.QTimer.singleShot(0, count)
    count()       
    mbox.exec_()
    
# ----------Window creation----------
app = QApplication([])
app.setStyle("Fusion")

w = QWidget()
w.setWindowTitle("UART serial values")
w.resize(300,300)

vb = QVBoxLayout(w)

lbl_com_b = QLabel(w)
lbl_com_b.setText("Serial Port:")
lbl_com_b.adjustSize()
vb.addWidget(lbl_com_b)

com_b = QComboBox(w)
com_b.addItems(serial_ports())
vb.addWidget(com_b)
com_b.activated.connect(set_serial_port)

lbl_bd_rate = QLabel(w)
lbl_bd_rate.setText("Baud Rate:")
vb.addWidget(lbl_bd_rate)

com_b_1 = QComboBox(w)
com_b_1.addItems(['9600', '1200', '2400', '4800',
                 '19200', '38400', '57600','115200'])
vb.addWidget(com_b_1)
com_b_1.activated.connect(set_baud_rate)

btn = QPushButton(w)
btn.setText('Enter')
vb.addWidget(btn)
btn.clicked.connect(dialog)

btn_stop = QPushButton(w)
btn_stop.setText('Stop')
vb.addWidget(btn_stop)
btn_stop.clicked.connect(QApplication.quit)

w.show()
app.exec_()