from Models.Climbers import Climbers
from Models.Model import Model

climber = Climbers()
print(climber.get())


for row, list in enumerate(climber.get()):
    print(row, ' - ', list)

for row, list in enumerate(climber.getOneField('name')):
    print(row,') ', list)

#climber.add()
climber.update(1, 'name', 35, 'egor')