from Models.Model import Model

class Climbers(Model):
    __nameTable = 'Climbers'
    __name = 'name'
    __address = 'address'

    def get(self):
        return super().get(self.__nameTable)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable,field)

    def add(self):
        name = input("Введите имя: ")
        address = input("Введите адрес: ")
        str =  f"{self.__name}, {self.__address}"
        super().add(self.__nameTable,str,name,address)

    def delete(self,id):
        super().delete(self.__nameTable,id)

    def update(self,table,field,id,values):
        super().update(self.__nameTable, field, values, id)