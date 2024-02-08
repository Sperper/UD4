import json
from jsonschema import validate

# Definir el esquema
schema = {
     "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
      "CFGS": {
        "type": "object",
        "properties": {
          "alumno": {
            "type": "array",
            "items": [
              {
                "type": "object",
                "properties": {
                  "NIF": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "resultado": {
                    "type": "array",
                    "items": [
                      {
                        "type": "object",
                        "properties": {
                          "$": {
                            "type": "object",
                            "properties": {
                              "resultado": {
                                "type": "string"
                              }
                            },
                            "required": [
                              "resultado"
                            ]
                          }
                        },
                        "required": [
                          "$"
                        ]
                      }
                    ]
                  },
                  "observaciones": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "MAC": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  }
                },
                "required": [
                  "NIF",
                  "resultado",
                  "observaciones",
                  "MAC"
                ]
              },
              {
                "type": "object",
                "properties": {
                  "NIF": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "resultado": {
                    "type": "array",
                    "items": [
                      {
                        "type": "object",
                        "properties": {
                          "$": {
                            "type": "object",
                            "properties": {
                              "resultado": {
                                "type": "string"
                              }
                            },
                            "required": [
                              "resultado"
                            ]
                          }
                        },
                        "required": [
                          "$"
                        ]
                      }
                    ]
                  },
                  "IP": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  }
                },
                "required": [
                  "NIF",
                  "resultado",
                  "IP"
                ]
              }
            ]
          }
        },
        "required": [
          "alumno"
        ]
      }
    },
    "required": [
      "CFGS"
    ]
}

# Archivo JSON a validar
archivo_json = '''
    {
  "CFGS": {
    "alumno": [
      {
        "NIF": [
          ""
        ],
        "resultado": [
          {
            "$": {
              "resultado": "apto"
            }
          }
        ],
        "observaciones": [
          ""
        ],
        "MAC": [
          ""
        ]
      },
      {
        "NIF": [
          ""
        ],
        "resultado": [
          {
            "$": {
              "resultado": "noApto"
            }
          }
        ],
        "IP": [
          ""
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