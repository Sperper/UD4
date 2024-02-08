import json
from jsonschema import validate

# Definir el esquema
schema = {

    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
      "CFGSDAM": {
        "type": "object",
        "properties": {
          "modulos": {
            "type": "array",
            "items": [
              {
                "type": "object",
                "properties": {
                  "nombre": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "contenidos": {
                    "type": "array",
                    "items": [
                      {
                        "type": "object",
                        "properties": {
                          "UD": {
                            "type": "array",
                            "items": [
                              {
                                "type": "object",
                                "properties": {
                                  "tipo": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  },
                                  "descripcion": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "tipo",
                                  "descripcion"
                                ]
                              }
                            ]
                          }
                        },
                        "required": [
                          "UD"
                        ]
                      }
                    ]
                  }
                },
                "required": [
                  "nombre",
                  "contenidos"
                ]
              }
            ]
          }
        },
        "required": [
          "modulos"
        ]
      }
    },
    "required": [
      "CFGSDAM"
    ]
  
}

# Archivo JSON a validar
archivo_json = '''
    {
  "CFGSDAM": {
    "modulos": [
      {
        "nombre": [
          ""
        ],
        "contenidos": [
          {
            "UD": [
              {
                "tipo": [
                  ""
                ],
                "descripcion": [
                  ""
                ]
              }
            ]
          }
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