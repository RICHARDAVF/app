from pandas import read_excel
from core.erp.models import CargoTrabajador,Trabajadores
class Cargo:
    def __init__(self):
        self.df  = read_excel(r"C:\Users\Lenovo\Desktop\proyecto\test\Personal de empresas del Edificio INMA.xlsx",dtype=str)
    def cargar(self):
        
       
        for item in self.df['CARGO'].to_list():
            try:
                car = CargoTrabajador(cargo=item)
                car.save()
            except Exception as e:
               pass
    def trabajadores(self):
        dni = self.df['DNI'].to_list()
        cargo = self.df['CARGO'].to_list()
        nombre = self.df['NOMBRE'].to_list()
        apellidos = self.df['APELLIDOS'].to_list()
        empresa = self.df['EMPRESA'].to_list()
        for doc,car,name,last,em in zip(dni,cargo,nombre,apellidos,empresa):
            tipo = "1"
            carg = CargoTrabajador.objects.get(cargo=car)
            if len(doc)!=8:
                tipo = '2'
            Trabajadores.objects.create(
                cargo=carg,
                tipo=tipo,
                documento=doc,
                nombre=name,
                apellidos=last,
                direccion='',
                empresa=em)