class Persona:
    def __init__(self, nombre, edad, telefono, direccion, correo ):
        self.__nombre = nombre
        self.__edad = edad
        self.__telefono = telefono
        self.__direccion = direccion
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def telefono(self):
        return self.__telefono

    @property
    def direccion(self):
        return self.__direccion

    @property
    def correo(self):
        return self.__correo

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre

    @edad.setter
    def edad(self, edad):
        self.__edad

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion

    @correo.setter
    def correo(self, correo):
        self.__correo



    def saludar(self):
        print(f"Hola yo soy {self.nombre} ")
    