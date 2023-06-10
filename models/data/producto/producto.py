class Producto:
    def __init__(self, nombre, identificador):
        self.nombre = nombre
        self.identificador = identificador
        self.versiones = []
    
    def agregar_version(self, version):
        self.versiones.append(version)
    
 
