# ==========================================
# 1. CLASE AUXILIAR PARA COMPOSICIÓN ("Tiene-un")
# ==========================================
class CredencialSeguridad:
    def __init__(self, id_token, metodo_2fa, activa=True):
        self.id_token = id_token
        self.metodo_2fa = metodo_2fa
        self.activa = activa

    def verificar_acceso(self):
        estado = "ACTIVA" if self.activa else "REVOCADA"
        return f"Token [{self.id_token}] | 2FA: {self.metodo_2fa} | Estado: {estado}"

    def revocar_token(self):
        self.activa = False
        return f"ALERTA: El token de seguridad [{self.id_token}] ha sido revocado."


# ==========================================
# 2. CLASE BASE (Con Composición y Encapsulamiento)
# ==========================================
class Empleado:
    def __init__(self, nombre, puesto, salario, proyectos_realizados, credencial):
        self.nombre = nombre
        self.puesto = puesto
        # Encapsulamiento: Atributo privado
        self.__salario = salario
        self.proyectos_realizados = proyectos_realizados
        # COMPOSICIÓN: Un Empleado "tiene-una" CredencialSeguridad
        self.credencial = credencial

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print(f"Error de validación: No se puede asignar un salario de ${nuevo_salario} a {self.nombre}.")

    def mostrar_info(self):
        print(f"Empleado: {self.nombre} | Puesto: {self.puesto} | Salario: ${self.salario:.2f} | Proyectos: {self.proyectos_realizados}")
        # Delegación de método hacia el objeto compuesto
        print(f"   └── Seguridad: {self.credencial.verificar_acceso()}")

    def aumentar_salario(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento
        print(f"[{self.nombre}] recibió un aumento del {porcentaje}%. Su nuevo salario es ${self.salario:.2f}.")

    def completar_proyecto(self, nombre_proyecto):
        self.proyectos_realizados += 1
        print(f"[{self.nombre}] completó el proyecto '{nombre_proyecto}'. Total de proyectos completados: {self.proyectos_realizados}.")


# ==========================================
# 3. SUBCLASE (Herencia y Polimorfismo)
# ==========================================
class LiderCiberseguridad(Empleado):
    def __init__(self, nombre, puesto, salario, proyectos_realizados, credencial, certificaciones, nivel_acceso):
        super().__init__(nombre, puesto, salario, proyectos_realizados, credencial)
        self.certificaciones = certificaciones
        self.nivel_acceso = nivel_acceso

    # Sobrescritura de método (Polimorfismo)
    def mostrar_info(self):
        print(f"Líder de Seguridad: {self.nombre} | Puesto: {self.puesto} | Salario: ${self.salario:.2f} | Proyectos: {self.proyectos_realizados} | Certificaciones: {self.certificaciones} | Nivel de Acceso: {self.nivel_acceso}")
        # Delegación de método hacia el objeto compuesto
        print(f"   └── Seguridad: {self.credencial.verificar_acceso()}")

    def auditar_sistema(self, sistema_objetivo):
        if self.credencial.activa:
            print(f"[{self.nombre}] ha iniciado una auditoría en '{sistema_objetivo}' usando {self.credencial.id_token} ({self.nivel_acceso}).")
        else:
            print(f"[ACCESO DENEGADO] {self.nombre} no puede auditar '{sistema_objetivo}' porque su credencial está revocada.")
