import sys

# import matplotlib.backends.backend_tkagg

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import numpy as np

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('OPS Analysis')
        self.setMinimumHeight(300)
        self.setMinimumWidth(650)
        self.setMaximumHeight(300)
        self.setMaximumWidth(650)
        self.setWindowIcon(QIcon('parachute.png'))  
        font = QFont() 
        font.setFamily("メイリオ")


        # Input画面
        layout_CdS1 = QHBoxLayout()
        self.label_CdS1 = QLabel('CdS1 [m^2]')
        self.textBox_CdS1 = QLineEdit()        
        layout_CdS1.addWidget(self.label_CdS1,1)
        layout_CdS1.addWidget(self.textBox_CdS1)
        
        layout_CdS1_Altitude = QHBoxLayout()
        self.label_CdS1_Altitude = QLabel("Open Altitude(CdS1) [m]") 
        self.textBox_CdS1_Altitude = QLineEdit()
        layout_CdS1_Altitude.addWidget(self.label_CdS1_Altitude,1)
        layout_CdS1_Altitude.addWidget(self.textBox_CdS1_Altitude)

        layout_CdS2 = QHBoxLayout()
        self.label_CdS2 = QLabel('CdS2 [m^2]')
        self.textBox_CdS2 = QLineEdit()
        layout_CdS2.addWidget(self.label_CdS2,1)
        layout_CdS2.addWidget(self.textBox_CdS2)

        layout_CdS2_Altitude = QHBoxLayout()
        self.label_CdS2_Altitude = QLabel("Open Altitude(CdS2) [m]")
        self.textBox_CdS2_Altitude = QLineEdit()
        layout_CdS2_Altitude.addWidget(self.label_CdS2_Altitude,1)
        layout_CdS2_Altitude.addWidget(self.textBox_CdS2_Altitude)

        layout_m = QHBoxLayout()
        self.label_m = QLabel("mass of Rocket [kg]")
        self.textBox_m = QLineEdit()
        layout_m.addWidget(self.label_m,1)
        layout_m.addWidget(self.textBox_m)

        layout_Pa0 = QHBoxLayout()
        self.label_Pa0 = QLabel("Atmospheric Pressure [hPa]")
        self.textBox_Pa0 = QLineEdit()
        layout_Pa0.addWidget(self.label_Pa0,1)
        layout_Pa0.addWidget(self.textBox_Pa0)

        layout_g0 = QHBoxLayout()
        self.label_g0 = QLabel("Gravity Acceleration [m/s^2]")
        self.textBox_g0 = QLineEdit()
        layout_g0.addWidget(self.label_g0,1)
        layout_g0.addWidget(self.textBox_g0)

        layout_T0 = QHBoxLayout()
        self.label_T0 = QLabel("Air Temperature [deg]")
        self.textBox_T0 = QLineEdit()
        layout_T0.addWidget(self.label_T0,1)
        layout_T0.addWidget(self.textBox_T0)

        layout_input = QVBoxLayout()
        layout_input.addLayout(layout_CdS1)
        layout_input.addLayout(layout_CdS1_Altitude)
        layout_input.addLayout(layout_CdS2)
        layout_input.addLayout(layout_CdS2_Altitude)
        layout_input.addLayout(layout_m)
        layout_input.addLayout(layout_Pa0)
        layout_input.addLayout(layout_g0)
        layout_input.addLayout(layout_T0)

        
        # Result 画面
        layout_V_CdS1 = QHBoxLayout()
        label_V_CdS1 = QLabel("Velocity(CdS1): ")
        self.result_V_CdS1 = QLabel("              ")
        self.result_V_CdS1.setContentsMargins(0, 0, 40, 0)  
        layout_V_CdS1.addWidget(label_V_CdS1)
        layout_V_CdS1.addWidget(self.result_V_CdS1)

        layout_V_CdS2 = QHBoxLayout()
        label_V_CdS2 = QLabel("Velocity(CdS2): ")
        self.result_V_CdS2 = QLabel("              ")
        self.result_V_CdS2.setContentsMargins(0, 0, 40, 0)          
        layout_V_CdS2.addWidget(label_V_CdS2)
        layout_V_CdS2.addWidget(self.result_V_CdS2)

        layout_OPS = QHBoxLayout()
        label_OPS = QLabel("OPS [N]: ")
        self.result_OPS = QLabel("              ")
        self.result_OPS.setContentsMargins(0, 0, 40, 0)          
        layout_OPS.addWidget(label_OPS)
        layout_OPS.addWidget(self.result_OPS)

        layout_status = QHBoxLayout()
        self.label_status = QLabel("status:")       
        self.result_status = QLabel("              ")
        layout_status.addWidget(self.label_status)
        layout_status.addWidget(self.result_status)
        


        # Calculationボタン
        button_Calculation = QPushButton("Calculation")
        button_Calculation.clicked.connect(self.calculationClicked)

        # 工事中ボタン
        self.button_Graph = QPushButton("Output Graph")
        self.button_Graph.clicked.connect(self.GraphClicked)
        self.button_Graph.setEnabled(False)

        # button_Graph

        layout_result = QVBoxLayout()
        layout_result.addLayout(layout_V_CdS1)
        layout_result.addLayout(layout_V_CdS2)
        layout_result.addLayout(layout_OPS)
        layout_result.addLayout(layout_status)
        layout_result.addWidget(button_Calculation)
        layout_result.addWidget(self.button_Graph)
        layout_result.addSpacing(20)
        

        # 画面の統合
        Hlayout = QHBoxLayout()
        Hlayout.addLayout(layout_input)
        Hlayout.addStretch(1)
        Hlayout.addLayout(layout_result)
        Hlayout.addStretch(1)
        

        self.setLayout(Hlayout)
        self.show()

    def calculationClicked(self):
        try:
            CdS1 = float(self.textBox_CdS1.text())
            Altitude_CdS1 = float(self.textBox_CdS1_Altitude.text())
            CdS2 = float(self.textBox_CdS2.text())
            Altitude_CdS2 = float(self.textBox_CdS2_Altitude.text())
            m = float(self.textBox_m.text())
            Pa0 = float(self.textBox_Pa0.text())
            g0 = float(self.textBox_g0.text())
            T0 = float(self.textBox_T0.text())
        except:
            self.result_status.setText("Input valid value")
            self.button_Graph.setEnabled(False)
            return
     
        dt = 0.01
        Z = Altitude_CdS1
        V = 0 
        t = 0
        self.tdata = np.array([])
        self.accdata = np.array([])
        self.Vdata = np.array([])

        CdS = CdS1
        while(True):
            T = T0 - 0.00649*Z
            Pa = Pa0*(1-(0.0065*Z/(T+0.0065*Z+273.15)))**5.257
            rho = Pa/(2.87*(T+273.15))
            g = g0  # debug
            acc = -g + 0.5*CdS*rho*V**2/m
            preV = V
            V = V + acc*dt
            Z = Z + V*dt
            t = t + dt
            self.tdata = np.append(self.tdata, t)
            self.accdata = np.append(self.accdata, acc*m)
            self.Vdata = np.append(self.Vdata, V)
            if(Z < Altitude_CdS2): 
                if(abs(acc) < 0.01):
                    self.result_status.setText("Altitude(CdS1) is too low!!")
                    self.button_Graph.setEnabled(False)
                    return
                else:
                    break
        
        self.result_V_CdS1.setText(str(round(-V,2))+"[m/s]")

        CdS = CdS2 + CdS1
        V = preV
        Z = Altitude_CdS2
        max_OPS = 0

        while(True):
            T = T0 - 0.00649*Z
            Pa = Pa0*(1-(0.0065*Z/(T+0.0065*Z+273.15)))**5.257
            rho = Pa/(2.87*(T+273.15))
            g = g0  # debug
            acc = -g + 0.5*CdS*rho*V**2/m
            preV = V
            V = V + acc*dt
            Z = Z + V*dt
            t = t + dt
            self.tdata = np.append(self.tdata, t)
            self.accdata = np.append(self.accdata, acc*m)
            self.Vdata = np.append(self.Vdata, V)
            if(max_OPS < acc*m): max_OPS = acc*m
            if(abs(acc) < 0.01): break
            if(Z<0): 
                self.result_status.setText("Altitude(CdS2) is too low!!")
                return


        self.result_status.setText("Complete!")
        self.button_Graph.setEnabled(True)
        self.result_V_CdS2.setText(str(round(-V,2))+"[m/s]")
        self.result_OPS.setText(str(round(max_OPS,2))+"[N]")
   
    def GraphClicked(self):
        savename = QFileDialog.getSaveFileName(self, filter="Image Files (*.png)")
            
        fig, (axL, axR) = plt.subplots(nrows=2, figsize=(8,6))

        axL.plot(self.tdata, self.accdata, linewidth=1)
        axL.set_xlabel('time[sec]')
        axL.set_ylabel('acceleration[m/s^2]')
        axL.set_xlim(0, self.tdata[-1])
        axL.grid(True)

        plt.subplots_adjust(wspace=0.4, hspace=0.6)

        axR.plot(self.tdata, self.Vdata, linewidth=1)
        axR.set_xlabel('time[sec]')
        axR.set_ylabel('Velocity[m/s]')
        axR.set_xlim(0, self.tdata[-1])
        axR.grid(True)

        plt.savefig(savename[0])
        
app = QApplication(sys.argv)
Page1 = Page1()
sys.exit(app.exec_())