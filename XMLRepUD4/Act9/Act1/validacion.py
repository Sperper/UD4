import json
from jsonschema import validate

# Definir el esquema
schema = {
     "$schema":"http://json-schema.org/draft-07/schema#",
    "type":"object",
    "properties": {
        "codigoDeLibro":{
            "type": "string",
            "minLength":13,
            "maxLength": 13
        },
        "titulo":{
            "type": "string",
            "minLength":1
        },
        "editorial":{
            "type": "string",
            "minLength":1
        },
        "edicion": {
            "type":"integer",
            "minLength":1
        },
        "ISBN": {
            "type":"string",
            "minLength":13,
            "maxLength":13
        },
        "numeroPaginas": {
            "type": "integer"
        },
        "autor": {
            "type": "string",
            "minLength": 1
        }
    }
}

# Archivo JSON a validar
archivo_json = '''
"codigoDeLibro": 9788420414065,
    "titulo": "La verdad sobre el caso Harry Quebert",
    "editorial": "ALFAGUARA",
    "edicion": 2013,
    "ISBN": "9788420414065",
    "numeroPaginas": 672,
    "autor": "Joel Dicker"
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.