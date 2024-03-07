from Data import Data

class FlyingModel(Data): # модель самолёта
    def flying(self, force): # физическая модель самолёта
        fe = force               # движущая сила, воздействие на самолёт изнутри(обороты пропеллера)
        fl = Data.startSpeed/2          
        acc = (Data.mass*Data.gravity + fl + fe)/Data.mass  # ускорение = (сила тяжести+инерция+сила воздействия на самолёт)/масса (второй закон Ньютона)
        Data.startSpeed += acc*Data.timeStep   # скорость(производная по ускорению)
        Data.startPosition += Data.startSpeed*Data.timeStep # перемещение: то, куда самолёт полетит под воздействием сил
        return Data.startPosition