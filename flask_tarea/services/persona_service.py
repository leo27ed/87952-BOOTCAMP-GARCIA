from models.persona import Persona


class PersonaService:

    def __init__(self, persona_repository):
        self.persona_repository = persona_repository

    def obtener_todos(self):

        personas = self.persona_repository.obtener_todos()

        return [persona.to_dict() for persona in personas]

    def obtener_por_dni(self, dni):

        persona = self.persona_repository.obtener_por_dni(dni)

        if not persona:
            return {
                "ok": False,
                "mensaje": "Persona no encontrada"
            }

        return {
            "ok": True,
            "data": persona.to_dict()
        }

    def crear(self, dni, nombre):

        # Regla de negocio:
        # no puede existir otra persona con el mismo DNI
        persona_existente = (
            self.persona_repository.obtener_por_dni(dni)
        )

        if persona_existente:
            return {
                "ok": False,
                "mensaje": "Ya existe una persona con ese DNI"
            }

        try:
            persona = Persona(dni, nombre)

        except ValueError as e:
            return {
                "ok": False,
                "mensaje": str(e)
            }

        self.persona_repository.agregar(persona)

        return {
            "ok": True,
            "data": persona.to_dict()
        }

    def actualizar(self, dni, nombre):

        persona_existente = (
            self.persona_repository.obtener_por_dni(dni)
        )

        if not persona_existente:
            return {
                "ok": False,
                "mensaje": "Persona no encontrada"
            }

        try:
            persona = Persona(dni, nombre)

        except ValueError as e:
            return {
                "ok": False,
                "mensaje": str(e)
            }

        self.persona_repository.actualizar(persona)

        return {
            "ok": True,
            "data": persona.to_dict()
        }

    def eliminar(self, dni):

        persona = self.persona_repository.obtener_por_dni(dni)

        if not persona:
            return {
                "ok": False,
                "mensaje": "Persona no encontrada"
            }

        self.persona_repository.eliminar(dni)

        return {
            "ok": True,
            "mensaje": "Persona eliminada correctamente"
        }