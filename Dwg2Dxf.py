import subprocess

ODA_RUTA = "C:\Program Files (x86)\ODA\Teigha File Converter 4.3.2\TeighaFileConverter"
CARPETA_ENTRADA = r"dwg"
CARPETA_SALIDA = r"output"
FORMAT_VER = "ACAD2018"
FORMATO_SALIDA = "DXF"
RECURSIVE = "0"
AUDIT = "1"
EXTENSION = "*.DWG"

comando = [ODA_RUTA, CARPETA_ENTRADA, CARPETA_SALIDA,
           FORMAT_VER, FORMATO_SALIDA, RECURSIVE, AUDIT, EXTENSION]

subprocess.run(comando, shell=True)
