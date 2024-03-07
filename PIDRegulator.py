from Data import Data

class PIDRegulator(Data): # ПИД-регулятор
    def computePID(self):      # функция вычисления необходимых оборотов с помощью ПИД-регулятора
        input = Data.modelY[-1]
        setPoint = Data.averageSmoothY[-1]
        err = setPoint - input
        Data.integralSum = Data.integralSum + err * Data.timeStep * Data.integralCoefficient      
        d = (err - Data.previousError) / Data.timeStep
        Data.previousError = err
        return err * Data.proportionalCoefficient + Data.integralSum + d * Data.derivativeCoefficient    