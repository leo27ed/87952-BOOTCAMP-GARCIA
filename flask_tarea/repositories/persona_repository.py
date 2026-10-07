class PersonaRepository:

    def __init__(self):
        self.personas = []

    def obtener_todos(self):
        return self.personas

    def obtener_por_dni(self, dni):
        for persona in self.personas:
            if persona.dni == str(dni):
                return persona

        return None

    def agregar(self, persona):
        self.personas.append(persona)

        return persona

    def actualizar(self, persona):
        for indice, persona_actual in enumerate(self.personas):

            if persona_actual.dni == persona.dni:
                self.personas[indice] = persona
                return persona

        return None

    def eliminar(self, dni):
        persona = self.obtener_por_dni(dni)

        if not persona:
            return False

        self.personas.remove(persona)

        return True