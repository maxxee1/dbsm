import csv

def ajustar_rut(input_file='C:/Code/dbsm/Datos_Cargar/rut.csv', output_file='rut_ajustado.csv'):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            rut = row[0]  
            rut = rut.strip()  
            
            if len(rut) > 10:
                rut = rut[:10]  
            elif len(rut) < 10:
                rut = rut.zfill(10) 
            
            row[0] = rut
            
            writer.writerow(row)

# Llamar a la función
ajustar_rut(input_file='C:/Code/dbsm/Datos_Cargar/rut.csv', output_file='rut_ajustado.csv')
