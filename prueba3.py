class Persona:
    def __init__(self, nombre, dpi):  
        self.nombre = nombre
        self.dpi = dpi

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, DPI: {self.dpi}")

class Estudiante(Persona):
    def __init__(self, nombre, dpi, carrera):  
        super().__init__(nombre, dpi)
        self.carrera = carrera

    def puede_entrar(self):
        carreras_cerradas = ["Pem", "Trabajo Social", "Mercadotecnia"]
        return self.carrera not in carreras_cerradas

class Profesor(Persona):
    def __init__(self, nombre, dpi, departamento):  
        super().__init__(nombre, dpi)
        self.departamento = departamento

    def puede_entrar(self):
        return True

class Visitante(Persona):
    def __init__(self, nombre, dpi, motivo_visita):  
        super().__init__(nombre, dpi)
        self.motivo_visita = motivo_visita

    def puede_entrar(self):
        return self.motivo_visita.lower() in ["investigación", "reunión"]


if __name__ == "__main__":  
    estudiante = Estudiante("Ana López", "1234567890101", "Mercadotecnia")
    profesor = Profesor("Carlos Gómez", "9876543210001", "Matemáticas")
    visitante = Visitante("Luis Pérez", "1928374650012", "reunión")

    personas = [estudiante, profesor, visitante]

    for persona in personas:
        persona.mostrar_datos()
        print("¿Puede entrar a la biblioteca?:", "Sí" if persona.puede_entrar() else "No")
        print("-" * 40)

