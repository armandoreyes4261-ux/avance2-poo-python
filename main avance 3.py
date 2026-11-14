from modelos import CredencialSeguridad, Empleado, LiderCiberseguridad

print("--- 1. CREACIÓN DE CREDENCIALES (Objetos Componentes) ---")
cred_carlos = CredencialSeguridad("TKN-1001", "App Autenticadora")
cred_armando = CredencialSeguridad("TKN-9001", "Llave Física YubiKey")
cred_laura = CredencialSeguridad("TKN-9002", "Biometría + YubiKey")

print("\n--- 2. INSTANCIACIÓN DE EMPLEADOS Y LÍDERES (Composición) ---")
emp1 = Empleado("Carlos Pérez", "Administrador de Redes", 20000, 2, cred_carlos)

lider1 = LiderCiberseguridad(
    "Armando Reyes García",
    "Analista de Ciberseguridad",
    30000,
    4,
    cred_armando,
    ["ISO 27001", "CEH"],
    "Tier 3 (Admin)"
)

lider2 = LiderCiberseguridad(
    "Laura Gómez",
    "Arquitecta de Seguridad",
    35000,
    6,
    cred_laura,
    ["CISSP", "CISM"],
    "Tier 4 (Root)"
)

print("\n--- 3. CONSULTA INICIAL (Polimorfismo + Delegación de Composición) ---")
emp1.mostrar_info()
lider1.mostrar_info()
lider2.mostrar_info()

print("\n--- 4. EJECUCIÓN DE ACCIONES, ENCAPSULAMIENTO Y COMPOSICIÓN ---")
# Prueba de encapsulamiento (setter con validación)
print("Intentando asignar un salario negativo...")
lider1.salario = -5000

# Acciones operativas
emp1.completar_proyecto("Migración de VLANs")
lider1.auditar_sistema("Servidor de Base de Datos Principal")
lider2.aumentar_salario(12)

# Prueba directa de interacción por Composición
print("\nRevocando credencial de Laura por protocolo de rotación...")
print(lider2.credencial.revocar_token())
lider2.auditar_sistema("Clúster de Producción")

print("\n--- 5. CONSULTA FINAL ---")
emp1.mostrar_info()
lider1.mostrar_info()
lider2.mostrar_info()
