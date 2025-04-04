# Etapa 1: Limpieza de Caracteres

En esta etapa, nos centramos en limpiar y estandarizar el archivo CSV antes de insertarlo en la base de datos. Realizamos varias transformaciones en los datos para asegurarnos de que estén en el formato correcto.

## ✅ Resumen de los cambios clave:

- **Paréntesis abierto, comilla simple, paréntesis cerrado, coma: ( '),  al inicio y final de cada línea.**
- **Reemplazo de barras `|` por comas `,`**
- **Eliminación de comillas de números.**
- **Modificación de RUTs de 6 a 12 dígitos, eliminando las comillas solo de los números.**

# Etapa 2: Condiciones y Restricciones de la Base de Datos

Antes de realizar el insert masivo de los datos, es importante asegurarnos de que cumplen con las condiciones y restricciones de la base de datos.

### 1. **Edades:**
   Las edades no pueden ser menores o iguales a 0. Se realiza una validación para filtrar esos registros y corregirlos si es necesario.

### 2. **RUTs Inválidos:**
   Verificamos que los RUTs estén dentro del rango correcto de dígitos (de 6 a 12 dígitos) y no contengan comillas alrededor de los números. Los registros con RUTs inválidos son descartados.


