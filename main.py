from ViajeroFrecuente import *
if __name__=='__main__':
    v=Viajero(123, 123232, 'Hernan', 'Quiroga', 732)

    v.mostrar()

    if 732 == v:
        print("La cantidad de millas es igual ")
    else:print("La cantidad de millas es diferente ")

    v = 100+v
    v.mostrar()

    v = 732-v
    v.mostrar()
