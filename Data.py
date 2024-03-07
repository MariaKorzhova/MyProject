from collections import deque
import random

class Data:
    
    timeStep = 0.02            # время в секундах одной итерации, отрисовывание каждой точки 
    
    # параметры для отрисовки графика
    graphicWindowSize = 100     # размер окна по Х
    pointMovedForward = 10      # на сколько точек будет выдвижен самолет относительно левой границы графика по Х
    
    # параметры туннелей и их изненения во время полёта
    tunnelLenght = 25           # начальная длина туннеля
    tunnelHeightMin = 30        # минимальная ширина (высота) туннеля (проём)
    acceleration = 200          # ускорение (укорочение длины туннеля (по оси Х) и минимальной ширины (по Y)) на reductionStep единиц через каждые 100 точек
    reductionStep = 1           # на сколько уменьшать
    ### верхняя и нижняя границы туннеля по Y, которые изменяются через tunnelLenght единиц
    lowTunnelEgde = random.randint(0,100-tunnelHeightMin) 
    upTunnelEgde = random.randint(lowTunnelEgde+tunnelHeightMin,100)

    # параметры для модели самолёта
    mass = 10 # масса
    gravity = -10 # ускорение свободного падения
    startPosition = 0 # начальная позиция
    startSpeed = 0 # начальная скорость

    # параметры для ПИД-регулятора
    proportionalCoefficient = 25
    integralCoefficient = 30
    derivativeCoefficient = 200
    integralSum, previousError = 0, 0  # вспомогательные параметры ПИД-регулятора

    averageLimit = 3            # расстояние, на которое среднее значение не должно приближатсья к краю туннеля

    ### блок задания списков (очередей) данных
    graphX= deque([i for i in range(-graphicWindowSize, 0)], maxlen = graphicWindowSize)  # ось Х окна графика
    lowEdgeY= deque([0]* graphicWindowSize, maxlen = graphicWindowSize) # нижняя граница туннеля по оси Y
    upEdgeY= deque([100]* graphicWindowSize, maxlen = graphicWindowSize) # верхняя граница туннеля по оси Y
    averageTunnelWidthY= deque([50]* graphicWindowSize, maxlen = graphicWindowSize) # среднее значение ширины туннеля по оси Y

    modelX = deque([i for i in range(-graphicWindowSize, -graphicWindowSize+pointMovedForward)], maxlen = pointMovedForward)  # ось X модели самолёта

    modelY = deque([0]* (pointMovedForward), maxlen = pointMovedForward) # ось Y модели самолёта

    averageSmoothY= deque([50]* (pointMovedForward), maxlen = pointMovedForward)  # "уставка" для ПИД регулятора, сглаженное среднее значение ширины туннеля по оси Y