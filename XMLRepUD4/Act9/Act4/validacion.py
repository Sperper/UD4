import json
from jsonschema import validate

# Definir el esquema
schema = {
     "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
      "Clientes": {
        "type": "object",
        "properties": {
          "sede": {
            "type": "array",
            "items": [
              {
                "type": "object",
                "properties": {
                  "dir1": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "dir2": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "codSede": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "empleado": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "fecha": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "cliente": {
                    "type": "array",
                    "items": [
                      {
                        "type": "object",
                        "properties": {
                          "codCliente": {
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
                          },
                          "numero": {
                            "type": "array",
                            "items": [
                              {
                                "type": "string"
                              }
                            ]
                          },
                          "coste": {
                            "type": "array",
                            "items": [
                              {
                                "type": "string"
                              }
                            ]
                          },
                          "resumen": {
                            "type": "array",
                            "items": [
                              {
                                "type": "string"
                              }
                            ]
                          },
                          "plazo": {
                            "type": "array",
                            "items": [
                              {
                                "type": "string"
                              }
                            ]
                          }
                        },
                        "required": [
                          "codCliente",
                          "descripcion",
                          "numero",
                          "coste",
                          "resumen",
                          "plazo"
                        ]
                      }
                    ]
                  }
                },
                "required": [
                  "dir1",
                  "dir2",
                  "codSede",
                  "empleado",
                  "fecha",
                  "cliente"
                ]
              }
            ]
          }
        },
        "required": [
          "sede"
        ]
      }
    },
    "required": [
      "Clientes"
    ]
}

# Archivo JSON a validar
archivo_json = '''
{
  "Clientes": {
    "sede": [
      {
        "dir1": [
          ""
        ],
        "dir2": [
          ""
        ],
        "codSede": [
          ""
        ],
        "empleado": [
          ""
        ],
        "fecha": [
          ""
        ],
        "cliente": [
          {
            "codCliente": [
              ""
            ],
            "descripcion": [
              ""
            ],
            "numero": [
              ""
            ],
            "coste": [
              ""
            ],
            "resumen": [
              ""
            ],
            "plazo": [
              ""
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