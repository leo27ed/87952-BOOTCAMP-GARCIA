class Persona:

    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        valor = str(valor).strip()

        if not valor:
            raise ValueError("El DNI es obligatorio")

        self._dni = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        valor = str(valor).strip()

        if not valor:
            raise ValueError("El nombre es obligatorio")

        if len(valor) > 30:
            raise ValueError(
                "El nombre no puede tener más de 30 caracteres"
            )

        if not valor[0].isupper():
            raise ValueError(
                "El nombre debe comenzar con mayúscula"
            )

        if len(valor) > 1 and not valor[1:].islower():
            raise ValueError(
                "Las demás letras del nombre deben ser minúsculas"
            )

        self._nombre = valor

    def to_dict(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre
        }