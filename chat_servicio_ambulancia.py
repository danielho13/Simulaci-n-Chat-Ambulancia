# === V0: Procedural, sin funciones ni clases ===
print("== Registro de caso ==")

# 1) Consentimiento
while True:
    r = input("Autoriza tratamiento de datos? [s/n]: ").strip().lower()
    if r in ("s", "si", "y", "yes"):
        consentimiento = True
        break
    if r in ("n", "no"):
        print("No se puede continuar sin consentimiento.")
        exit()
    print("Respuesta inválida.")

# 2) Cobertura (11,12,13) múltiple
permitidos = {11, 12, 13}
while True:
    raw = input("Cobertura (opciones 11,12,13; sep. por coma): ").strip()
    try:
        cobertura = [int(x) for x in raw.split(",") if x.strip()]
        if cobertura and all(c in permitidos for c in cobertura):
            break
    except ValueError:
        pass
    print("Entrada inválida. Ej: 11,13")

# 3) Tipo cliente 1..3
op_tc = {1: "Clínica", 2: "Familiar", 3: "Reporte Emergencia"}
while True:
    try:
        tipo_cliente = int(input("Tipo de cliente (1 Clínica, 2 Familiar, 3 Reporte Emergencia): "))
        if tipo_cliente in op_tc: break
    except ValueError: pass
    print("Opción inválida.")

# 4) Datos solicitante
while True:
    ced_sol = input("Solicitante - Cédula (solo números): ").strip()
    if ced_sol.isdigit(): break
    print("Cédula inválida.")
nom_sol = input("Solicitante - Nombre completo: ").strip()
while True:
    tel_sol = input("Solicitante - Teléfono (10 dígitos): ").strip()
    if tel_sol.isdigit() and len(tel_sol) == 10: break
    print("Teléfono inválido.")

# 5) Datos paciente
while True:
    ced_pac = input("Paciente - Cédula (solo números): ").strip()
    if ced_pac.isdigit(): break
    print("Cédula inválida.")
nom_pac = input("Paciente - Nombre completo: ").strip()
while True:
    tel_pac = input("Paciente - Teléfono (10 dígitos): ").strip()
    if tel_pac.isdigit() and len(tel_pac) == 10: break
    print("Teléfono inválido.")
eps_pac = input("Paciente - EPS: ").strip()

# 6) Tipo servicio 1..3
op_ts = {1: "Traslado", 2: "Primeros auxilios", 3: "Reporte accidente de un tercero"}
while True:
    try:
        tipo_serv = int(input("Tipo de servicio (1 Traslado, 2 Primeros auxilios, 3 Reporte tercero): "))
        if tipo_serv in op_ts: break
    except ValueError: pass
    print("Opción inválida.")

# 7) Triage 1..4
while True:
    try:
        triage = int(input("Estado paciente (Triage 1,2,3,4): "))
        if triage in (1,2,3,4): break
    except ValueError: pass
    print("Opción inválida.")

# 8) Encuentro y 9) Destino
encuentro = input("Lugar del encuentro (dirección o referencia): ").strip()
destino   = input("Destino (clínica/dirección): ").strip()

# Regla simple de prioridad
emergencia = (tipo_cliente == 3) or (triage in (1,2))

# Resumen
print("\n== Resumen ==")
print(f"- Consentimiento: Sí")
print(f"- Cobertura: {cobertura}")
print(f"- Tipo de cliente: {op_tc[tipo_cliente]}")
print(f"- Solicitante: {nom_sol} | Céd: {ced_sol} | Tel: {tel_sol}")
print(f"- Paciente: {nom_pac} | Céd: {ced_pac} | Tel: {tel_pac} | EPS: {eps_pac}")
print(f"- Tipo de servicio: {op_ts[tipo_serv]}")
print(f"- Triage: {triage}")
print(f"- Encuentro: {encuentro}")
print(f"- Destino: {destino}")
print(f"- Emergencia: {'Sí' if emergencia else 'No'}")

# Confirmación
while True:
    ok = input("¿Confirmar? [s/n]: ").strip().lower()
    if ok in ("s","si","y","yes"):
        print("✅ Caso confirmado (simulado).")
        break
    if ok in ("n","no"):
        print("❌ Cancelado.")
        break
    print("Respuesta inválida.")
