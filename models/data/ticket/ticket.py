from models.data.historial.historial import Historial

class Ticket:
    def __init__(self, titulo, descripcion, prioridad, severidad, fechaCreacion, horaCreacion, cliente, nivelSoporte, encargado, horas, identificador):
        self.identificador = identificador
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.severidad = severidad
        self.fechaCreacion = fechaCreacion
        self.horaCreacion = horaCreacion
        self.cliente = cliente
        self.estado = "Abierto"
        self.nivelSoporte = nivelSoporte
        self.encargado = encargado
        self.historial = Historial()
        self.horas = horas
        self.tareas = []
        
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def agregar_historia(self, historia):
        self.historial.agregar_historia(historia)
    
    # Getters para los atributos inmodificables
    def get_fechaCreacion(self):
        return self.fechaCreacion
    
    def get_horaCreacion(self):
        return self.horaCreacion
    
    def get_horas(self):
        return self.horas

    # Getter y Setter para el atributo "prioridad"
    def get_prioridad(self):
        return self.prioridad

    def set_prioridad(self, prioridad):
        self.prioridad = prioridad
    
    # Getter y Setter para el atributo "severidad"
    def get_severidad(self):
        return self.severidad
    
    def set_severidad(self, severidad):
        self.severidad = severidad
    
    # Getter y Setter para el atributo "descripcion"
    def get_descripcion(self):
        return self.descripcion
    
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
    
    # Getter y Setter para el atributo "titulo"
    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, titulo):
        self.titulo = titulo

    # Getter y Setter para el atributo "estado"
    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    # Getter y Setter para el atributo "nivelSoporte"
    def get_nivelSoporte(self):
        return self.nivelSoporte

    def set_nivelSoporte(self, nivelSoporte):
        self.nivelSoporte = nivelSoporte

    # Getter y Setter para el atributo "encargado"
    def get_encargado(self):
        return self._encargado
    
    def set_encargado(self, encargado):
        self._encargado = encargado
