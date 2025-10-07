# Chat de Registro de Servicio de Ambulancia 🚑💬

Proyecto académico en Python que simula un **chat interactivo por consola** para registrar solicitudes de atención médica o servicios de ambulancia.  
El sistema guía paso a paso al operador, validando la información ingresada y generando un resumen estructurado del caso.

---

## 🧠 Descripción general

Este proyecto representa la primera versión (**V0**) del sistema, implementada **sin funciones ni clases**, de forma **procedimental**, ideal para aprender:

- Flujo secuencial de un programa en Python  
- Validación de entradas (`input()`)  
- Control de errores mediante ciclos `while` y excepciones  
- Impresión de reportes y confirmaciones

---

## 🏥 Flujo del programa

El sistema guía al usuario por los siguientes pasos:

1. **Consentimiento de tratamiento de datos** (obligatorio).  
2. **Selección de cobertura** (una o varias zonas disponibles: 11, 12, 13).  
3. **Tipo de cliente:**  
   - `1`: Clínica  
   - `2`: Familiar  
   - `3`: Reporte de emergencia  
4. **Datos del solicitante:** cédula, nombre y teléfono.  
5. **Datos del paciente:** cédula, nombre, teléfono y EPS.  
6. **Tipo de servicio solicitado:**  
   - `1`: Traslado  
   - `2`: Primeros auxilios  
   - `3`: Reporte de accidente de un tercero  
7. **Triage (estado del paciente)** de 1 a 4.  
8. **Lugar de encuentro** y **destino final**.  
9. **Evaluación de prioridad:** se marca como *emergencia* si el tipo de cliente es 3 o el triage ≤ 2.  
10. **Confirmación final** del caso.

---

## 💻 Ejemplo de ejecución

```
== Registro de caso ==
Autoriza tratamiento de datos? [s/n]: s
Cobertura (opciones 11,12,13; sep. por coma): 11,13
Tipo de cliente (1 Clínica, 2 Familiar, 3 Reporte Emergencia): 2
Solicitante - Cédula (solo números): 1098765432
Solicitante - Nombre completo: Juan Pérez
Solicitante - Teléfono (10 dígitos): 3204567890
Paciente - Cédula (solo números): 1234567890
Paciente - Nombre completo: María Gómez
Paciente - Teléfono (10 dígitos): 3109876543
Paciente - EPS: NuevaEPS
Tipo de servicio (1 Traslado, 2 Primeros auxilios, 3 Reporte tercero): 1
Estado paciente (Triage 1,2,3,4): 3
Lugar del encuentro (dirección o referencia): Calle 45 #10-22
Destino (clínica/dirección): Clínica Central

== Resumen ==
- Consentimiento: Sí
- Cobertura: [11, 13]
- Tipo de cliente: Familiar
- Solicitante: Juan Pérez | Céd: 1098765432 | Tel: 3204567890
- Paciente: María Gómez | Céd: 1234567890 | Tel: 3109876543 | EPS: NuevaEPS
- Tipo de servicio: Traslado
- Triage: 3
- Encuentro: Calle 45 #10-22
- Destino: Clínica Central
- Emergencia: No
¿Confirmar? [s/n]: s
✅ Caso confirmado (simulado).
```

---

## 🧩 Requisitos

- Python **3.10 o superior**
- No requiere librerías externas.

---

## 🗂️ Estructura sugerida

```
chat_servicio_ambulancia/
├─ chat_servicio_ambulancia.py
├─ README.md
├─ .gitignore
└─ LICENSE
```

---

## 🛠️ Posibles mejoras

- [ ] Modularizar con **funciones** para cada sección (datos, validación, resumen).  
- [ ] Migrar a una **versión con clases** (`Caso`, `Paciente`, `Solicitante`).  
- [ ] Agregar almacenamiento en archivo o base de datos (JSON o SQLite).  
- [ ] Implementar interfaz web o GUI simple.  
- [ ] Añadir logs automáticos y marca temporal.

---

démicos o de aprendizaje.
