import time

contraseñas = ["abc123", "qwerty", "123456", "password", "gatito123", "hola123"]
objetivo = "gatito123"

tiempo_inicio = time.time()

for c in contraseñas:
    if c == objetivo:
        break

tiempo_fin = time.time()
tiempo_encontrar_password = tiempo_fin - tiempo_inicio

print("Tiempo total en encontrar la contraseña:", tiempo_encontrar_password, "segundos")
print(f"{ tiempo_encontrar_password * 1_000_000:.2f} microsegundos")

