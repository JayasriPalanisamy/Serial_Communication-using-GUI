from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import serial
import sys

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

# Creating main window
class Window(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.win = QWidget()
        self.win.setGeometry(500, 200, 300, 250)
        self.win.setWindowTitle("UART serial values")
        super().__init__()

        # creating form
        self.formGroupBox = QGroupBox("Parameters:")
        self.layout = QFormLayout()
        self.com_b_1 = QComboBox()
        self.com_b_1.addItems(serial_ports())
        self.com_b_2 = QComboBox()
        self.com_b_2.addItems(['9600', '1200', '2400', '4800',
                        '19200', '38400', '57600','115200'])
        self.layout.addRow(QLabel("COM Port:"),self.com_b_1)
        self.layout.addRow(QLabel("Baudrate:"),self.com_b_2)
        self.formGroupBox.setLayout(self.layout)

        self.com_b_1.activated.connect(self.set_serial_port)
        self.com_b_2.activated.connect(self.set_baud_rate)

        # creating display region
        self.formGroupBox_1 = QGroupBox("Serial Values:")
        self.layout_1 = QHBoxLayout()
        self.lbl = QLabel()
        self.layout_1.addWidget(self.lbl)
        self.formGroupBox_1.setLayout(self.layout_1)

        # Setting selection buttons
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.formGroupBox)
        self.mainLayout.addWidget(self.buttonBox)
        self.mainLayout.addWidget(self.formGroupBox_1)
        self.buttonBox.accepted.connect(self.add_form)
        self.win.setLayout(self.mainLayout)

        self.win.show()
        sys.exit(self.app.exec_())

    def add_form(self):
        self.serialPort = serial.Serial(port=serial_port_para['port'], 
                            baudrate=int(serial_port_para['baudrate']),
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=8, timeout=2)
        def count():
            data = self.serialPort.readline()
            data1 = data[:-2].decode("utf-8")
            self.lbl.setText(f"{data1}")
            QtCore.QTimer.singleShot(2, count)
            
        count()

    def set_serial_port(self):
        serial_port_para['port'] = self.com_b_1.currentText()

    def set_baud_rate(self):
        serial_port_para['baudrate'] = self.com_b_2.currentText()

win = Window()

