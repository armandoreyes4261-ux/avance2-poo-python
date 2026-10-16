"""
Sistema de Gestión de Empleados
Este script modela empleados generales y líderes de ciberseguridad, 
aplicando principios de Encapsulamiento, Herencia y Polimorfismo.
"""

# Creación de la clase base
class Empleado:
    def __init__(self, nombre, puesto, salario, proyectos_realizados):
        self.nombre = nombre
        self.puesto = puesto
        # Aplicación de Encapsulamiento: Atributo privado usando doble guion bajo
        self.__salario = salario 
        self.proyectos_realizados = proyectos_realizados

    # Getters y Setters para controlar el acceso al atributo privado de forma segura
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print(f"Error de validación: No se puede asignar un salario de ${nuevo_salario} a {self.nombre}.")

    # Comportamiento general
    def mostrar_info(self):
        print(f"Empleado: {self.nombre} | Puesto: {self.puesto} | Salario: ${self.salario:.2f} | Proyectos: {self.proyectos_realizados}")

    def aumentar_salario(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario += aumento # Utiliza el setter con validación
        print(f"[{self.nombre}] recibió un aumento del {porcentaje}%. Su nuevo salario es ${self.salario:.2f}.")

    def completar_proyecto(self, nombre_proyecto):
        self.proyectos_realizados += 1
        print(f"[{self.nombre}] completó el proyecto '{nombre_proyecto}'. Total de proyectos completados: {self.proyectos_realizados}.")

# Uso de super() y Herencia
class LiderCiberseguridad(Empleado):
    def __init__(self, nombre, puesto, salario, proyectos_realizados, certificaciones, nivel_acceso):
        # Heredamos los atributos de la superclase
        super().__init__(nombre, puesto, salario, proyectos_realizados)
        # Añadimos 2 atributos nuevos propios de la subclase
        self.certificaciones = certificaciones
        self.nivel_acceso = nivel_acceso

    # Sobrescritura de métodos (Polimorfismo)
    def mostrar_info(self):
        print(f" Líder de Seguridad: {self.nombre} | Puesto: {self.puesto} | Salario: ${self.salario:.2f} | Proyectos: {self.proyectos_realizados} | Certificaciones: {self.certificaciones} | Nivel de Acceso: {self.nivel_acceso}")

    # Método operativo adicional propio de la subclase
    def auditar_sistema(self, sistema_objetivo):
        print(f"[{self.nombre}] ha iniciado una auditoría de seguridad en '{sistema_objetivo}' utilizando privilegios de nivel '{self.nivel_acceso}'.")


# ==========================================
# Instanciación y pruebas
# ==========================================

print("--- INSTANCIACIÓN DE 3 OBJETOS DISTINTOS ---")
# 1. Instancia de la clase base
emp1 = Empleado("Carlos Pérez", "Administrador de Redes", 20000, 2)

# 2. Instancias de la subclase
lider1 = LiderCiberseguridad("Armando Reyes García", "Analista de Ciberseguridad", 30000, 4, ["ISO 27001", "CEH"], "Tier 3 (Admin)")
lider2 = LiderCiberseguridad("Laura Gómez", "Arquitecta de Seguridad", 35000, 6, ["CISSP", "CISM"], "Tier 4 (Root)")

print("\n--- CONSULTA INICIAL (Demostrando Polimorfismo) ---")
emp1.mostrar_info()    # Ejecuta el método original
lider1.mostrar_info()  # Ejecuta el método sobrescrito
lider2.mostrar_info()

print("\n--- EJECUCIÓN DE ACCIONES Y ENCAPSULAMIENTO ---")
# Probando la restricción del setter (Encapsulamiento)
print("Intentando asignar un salario negativo...")
lider1.salario = -5000 

# Acciones exclusivas demostrando independencia
emp1.completar_proyecto("Migración de VLANs")
lider1.auditar_sistema("Servidor de Base de Datos Principal")
lider2.aumentar_salario(12)

print("\n--- CONSULTA FINAL ---")
emp1.mostrar_info()
lider1.mostrar_info()
lider2.mostrar_info()
