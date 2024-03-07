import threading
from PyQt5.QtWidgets import QApplication, QPushButton
import sys
from Processing import Processing
from FlyingModel import FlyingModel
from PIDRegulator import PIDRegulator
from Graphic import Graphic

def autopilot(): 
    # назначение экземпляров класса и счётчика
    ourGraph = Graphic() 
    ourProc = Processing()
    ourSamolet = FlyingModel() 
    ourPID = PIDRegulator() 
    i = 0
    while True:
        engineSpeed = ourPID.computePID()  # вычисления нужных оборотов для самолета с помощью ПИД-регулятора
        NewModelPos = ourSamolet.flying(engineSpeed) # вычисление новой позиции модели после применения новых оборотов пропеллера, равных engineSpeed
        ourProc.updateData(NewModelPos, i) # обновляем данные
        ourGraph.updateGraphic() # обновляем график
        ourProc.checkAndDelay()
        i += 1


if __name__ == "__main__":       
    # кнопка "Выйти"
    app = QApplication(sys.argv) 
    def endFlyingByButton():           
        Processing.buttonExit()
    btn = QPushButton('Exit') 
    btn.clicked.connect(endFlyingByButton)
    btn.show()

    autopilotThread = threading.Thread(target=autopilot()) # запуск функции autopilot в отдельном потоке
    autopilotThread.start()




