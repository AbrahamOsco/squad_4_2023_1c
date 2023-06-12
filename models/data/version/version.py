class Version:
    def __init__(self, numero, identificador):
        self.numero = numero
        self.identificador = identificador
        self.tickets = []
    
    def agregar_ticket(self, ticket):
        self.tickets.append(ticket)
