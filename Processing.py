from Data import Data
from Graphic import Graphic
import random
import time

class Processing(Data):
    # генерация новых границ туннеля
    def randoms(self):
        lowTunnelEgdeOld = self.lowTunnelEgde
        self.lowTunnelEgde = random.randint(max(lowTunnelEgdeOld-2*self.tunnelHeightMin, 0),self.upTunnelEgde-self.tunnelHeightMin)
        self.upTunnelEgde = random.randint(max(self.lowTunnelEgde+self.tunnelHeightMin,lowTunnelEgdeOld+self.tunnelHeightMin),min(self.upTunnelEgde+2*self.tunnelHeightMin, 100))
    # обновление данных
    def updateData(self, newModelPosition, nextX):
        self.graphX.append(nextX) # следующая точка по Х 
        self.lowEdgeY.append(self.lowTunnelEgde)
        self.upEdgeY.append(self.upTunnelEgde)
        self.averageTunnelWidthY.append((self.lowTunnelEgde + self.upTunnelEgde)/2)
        
        aveSmoothSum = sum(list(self.averageTunnelWidthY)[-self.graphicWindowSize+self.pointMovedForward:-self.graphicWindowSize+self.pointMovedForward+self.tunnelLenght])/self.tunnelLenght  #вычисление среднего значения tunnelLenght вперёд идущих точек
        # проверка близости сглаженного среднего к границе туннеля
        if aveSmoothSum < self.lowEdgeY[-self.graphicWindowSize+self.pointMovedForward]+self.averageLimit:
            self.averageSmoothY.append(self.lowEdgeY[-self.graphicWindowSize+self.pointMovedForward]+self.averageLimit)
        elif aveSmoothSum > self.upEdgeY[-self.graphicWindowSize+self.pointMovedForward]-self.averageLimit:
            self.averageSmoothY.append(self.upEdgeY[-self.graphicWindowSize+self.pointMovedForward]-self.averageLimit)
        else:
            self.averageSmoothY.append(aveSmoothSum)
    
        self.modelX.append(self.graphX[-self.graphicWindowSize+self.pointMovedForward])
        self.modelY.append(newModelPosition)

    def checkAndDelay(self):
        # проверка выхода самолёта за границы туннеля
        if self.modelY[-1] >= self.upEdgeY[-self.graphicWindowSize+self.pointMovedForward] or self.modelY[-1] <= self.lowEdgeY[-self.graphicWindowSize+self.pointMovedForward]:
            print('Полет окончен (」°ロ°)」Счёт — ', self.graphX[-1] + 1 + self.pointMovedForward-self.graphicWindowSize)
            Graphic.writeFinalFrame(self)           # сохранение картинки перед "крушением"
            exit()                                  # завершение полёта
        else:
            if self.graphX[-1] % self.tunnelLenght == 0 and self.graphX[-1] != 0:       # проверка, когда необходимо генерировать новые рандомные границы
                self.randoms()
            if self.graphX[-1] % self.acceleration == 0 and self.graphX[-1] != 0:       # проверка условия ускорения
                if self.tunnelLenght - self.reductionStep > 0:  # ограничение уменьшения длины туннеля
                    self.tunnelLenght -= self.reductionStep     # уменьшение длины туннеля
                else: pass
                if self.tunnelHeightMin - self.reductionStep > 0:           # ограничение уменьшения минимальной высоты туннеля
                    self.tunnelHeightMin -= self.reductionStep              # уменьшение минимальной высоты туннеля
                else: pass
            time.sleep(self.timeStep)
    @classmethod
    def buttonExit(self): 
        print('Полет окончен досрочно ⸜( ´ ꒳ ` )⸝ Счёт — ', self.graphX[-1] + 1 + self.pointMovedForward-self.graphicWindowSize)
        Graphic.writeFinalFrame(self)        # сохранение картинки перед "крушением" или выходом
        exit()