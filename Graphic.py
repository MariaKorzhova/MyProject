import matplotlib.pyplot as plt
from Data import Data
import os

class Graphic(Data):

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.clear()
    plt.ylim([-1, 101])       # окно графика по Y
    lowTunnelBorder, = ax.plot(list(Data.graphX), list(Data.lowEdgeY), '_-k', ms=2, label='lowEdge')   # тут и далее отрисовка линий
    upTunnelBorder, = ax.plot(list(Data.graphX), list(Data.upEdgeY), '_-k', ms=2, label='upEdge')

    modelTail, = ax.plot(list(Data.modelX), list(Data.modelY), 'o-r', ms=2, label='tail') # шлейф самолёта
    modelHead, = ax.plot(list(Data.modelX)[-1], list(Data.modelY)[-1], '>-k', ms=15, label='airplan') # модель самолёта
    
    def updateGraphic(self):
        self.lowTunnelBorder.set_xdata(list(self.graphX))    # тут и далее обновляем данные на графике 
        self.lowTunnelBorder.set_ydata(list(self.lowEdgeY))
        self.upTunnelBorder.set_xdata(list(self.graphX))
        self.upTunnelBorder.set_ydata(list(self.upEdgeY))

        self.modelTail.set_xdata(list(self.modelX))
        self.modelTail.set_ydata(list(self.modelY))

        self.modelHead.set_xdata(list(self.modelX)[-1])
        self.modelHead.set_ydata(list(self.modelY)[-1])

        plt.xlim([self.graphX[-1]-self.graphicWindowSize, self.graphX[-1]]) # обновляется ось Х, так как на каждом шагу смещение графика, то и границы графика смещаются

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def writeFinalFrame(self): # сохранение текущего графика как файл .png после окончания полёта 
        plt.savefig(os.path.dirname(os.path.abspath(__file__)) + '\LastResult.png')
        plt.close('all')