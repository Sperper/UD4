import json
from jsonschema import validate

# Definir el esquema
schema = {
     "$schema":"http://json-schema.org/draft-07/schema#",
    "type":"object",
    "properties": {
        "condigoDeCoche": {
            "type": "string",
            "minimum": 17,
            "maxLength": 17
        },
        "marca": {
            "type":"string"
        
        },
        "modelo": {
            "type":"string"
        }
    }
}

# Archivo JSON a validar
archivo_json = '''
{
  "Concesionario": {
    "coche": [
      {
        "codigoDeCoche": [
          "IJCLMNJHG89736589"
        ],
        "marca": [
          "Ferrari"
        ],
        "modelo": [
          "Ferrari SF90 Stradale"
        ],
        "matricula": [
          "7865 ETF"
        ],
        "potencia": [
          "1000CV"
        ],
        "plazas": [
          "2"
        ],
        "numeroDePuertas": [
          "2"
        ]
      },
      {
        "codigoDeCoche": [
          "IKCLMNJOG83736589"
        ],
        "marca": [
          "Lamborghini"
        ],
        "modelo": [
          "Urus S"
        ],
        "matricula": [
          "5287 PDP"
        ],
        "potencia": [
          "666CV"
        ],
        "plazas": [
          "5"
        ],
        "numeroDePuertas": [
          "5"
        ]
      }
    ]
  }
}
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.