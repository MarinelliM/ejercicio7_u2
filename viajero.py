class Viajero:
    __numv=""
    __dni=""
    __nombre=""
    __apellido=""
    __millasa=""

    def __init__(self,num,dni,nom,ap,millas):
        self.__numv=num
        self.__dni=dni
        self.__nombre=nom
        self.__apellido=ap
        self.__millasa=millas

    def __gt__(self,other):
        if self.__millasa > other:
            return True
        else :return False

    def __eq__(self, other):
        if self.__millasa == other:
            return True
        else:False

    def __add__(self, other):
        self.__millasa+other
        print("Millas acumuladas")
        return Viajero(self.__numv, self.__dni, self.__nombre, self.__apellido, self.__millasa+other)

    def __radd__(self, other):
        self.__millasa+other
        print("Millas acumuladas")
        return Viajero(self.__numv, self.__dni, self.__nombre, self.__apellido, self.__millasa+other)

    def __sub__(self, other):
        if other <= self.__millas_acum:
            print("Millas canjeadas")
            self.__millasa-other
            return Viajero(self.__numv,self.__dni,self.__nombre,self.__apellido,self.__millasa-other)
        else: print("Millas insuficientes")

    def __rsub__(self, other):
        if self.__millasa <= other:
            print("Millas canjeadas")
            other-self.__millasa
            return Viajero(self.__numv,self.__dni,self.__nombre,self.__apellido,other-self.__millasa)
        else: print("Millas insuficientes")

     def mostrar(self):
        print('-'*50)
        print('numero de viajero: {}'.format(self.__numv))
        print("dni del viajero: {}".format(self.__dni))
        print("nombre: {}".format(self.__nombre))
        print("apellido: {}".format(self.__apellido))
        print('millas acumaldas del viajero: {}'.format(self.__millasa))
        print('-'*50)
