import csv

def procesar_datos(input_file='C:/Code/dbsm/Datos_Cargar/masivoo.sql', output_file='salida.sql'):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        # Preparamos el encabezado del archivo SQL de salida
        outfile.write("INSERT INTO persona1 (RUT, Nombre, Edad, Direccion) VALUES\n")

        # Procesar cada fila del archivo CSV
        for row in reader:
            RUT = row[0].strip()  
            Nombre = row[1].strip()  
            Edad = row[2].strip()  
            Direccion = row[3].strip()  

            # Asegurarse de que el RUT tenga 10 dígitos, agregando ceros al final si es menor
            if len(RUT) < 10:
                RUT = RUT.ljust(10, '0')  # Añadir ceros al final del RUT hasta que tenga 10 dígitos

            # Formatear cada fila en el formato SQL (con comillas simples para cadenas)
            insert_statement = f"({RUT},'{Nombre}',{Edad},'{Direccion}'),\n"
            outfile.write(insert_statement)

# Llamar a la función
procesar_datos(input_file='C:/Code/dbsm/Datos_Cargar/masivoo.sql', output_file='salida.sql')
