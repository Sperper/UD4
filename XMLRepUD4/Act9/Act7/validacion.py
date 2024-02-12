import json
from jsonschema import validate

# Definir el esquema
schema = {
    "numeroschema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
      "Informe": {
        "type": "object",
        "properties": {
          "cabecera": {
            "type": "array",
            "items": [
              {
                "type": "object",
                "properties": {
                  "descripcion": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  },
                  "fechaInforme": {
                    "type": "array",
                    "items": [
                      {
                        "type": "string"
                      }
                    ]
                  }
                },
                "required": [
                  "descripcion",
                  "fechaInforme"
                ]
              }
            ]
          },
          "datos": {
            "type": "array",
            "items": [
              {
                "type": "object",
                "properties": {
                  "region": {
                    "type": "array",
                    "items": [
                      {
                        "type": "object",
                        "properties": {
                          "zona": {
                            "type": "array",
                            "items": [
                              {
                                "type": "string"
                              }
                            ]
                          },
                          "trimestre": {
                            "type": "array",
                            "items": [
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                      "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                      "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                      "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                      "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              }
                            ]
                          }
                        },
                        "required": [
                          "zona",
                          "trimestre"
                        ]
                      },
                      {
                        "type": "object",
                        "properties": {
                          "zona": {
                            "type": "array",
                            "items": [
                              {
                                "type": "string"
                              }
                            ]
                          },
                          "trimestre": {
                            "type": "array",
                            "items": [
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                      "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                       "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                      "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                      "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              }
                            ]
                          }
                        },
                        "required": [
                          "zona",
                          "trimestre"
                        ]
                      },
                      {
                        "type": "object",
                        "properties": {
                          "zona": {
                            "type": "array",
                            "items": [
                              {
                                "type": "string"
                              }
                            ]
                          },
                          "trimestre": {
                            "type": "array",
                            "items": [
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                      "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                      "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                      "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              },
                              {
                                "type": "object",
                                "properties": {
                                  "numero": {
                                    "type": "object",
                                    "properties": {
                                      "numero": {
                                        "type": "string"
                                      }
                                    },
                                    "required": [
                                      "numero"
                                    ]
                                  },
                                  "librosVendidos": {
                                    "type": "array",
                                    "items": [
                                      {
                                        "type": "string"
                                      }
                                    ]
                                  }
                                },
                                "required": [
                                  "numero",
                                  "librosVendidos"
                                ]
                              }
                            ]
                          }
                        },
                        "required": [
                          "zona",
                          "trimestre"
                        ]
                      }
                    ]
                  }
                },
                "required": [
                  "region"
                ]
              }
            ]
          }
        },
        "required": [
          "cabecera",
          "datos"
        ]
      }
    },
    "required": [
      "Informe"
    ]
}

# Archivo JSON a validar
archivo_json = '''
    {
  "Informe": {
    "cabecera": [
      {
        "descripcion": [
          "informe de ventas para las regiones Norte, Centro y Sur"
        ],
        "fechaInforme": [
          "30/12/2009"
        ]
      }
    ],
    "datos": [
      {
        "region": [
          {
            "zona": [
              "Norte"
            ],
            "trimestre": [
              {
                "numero": {
                  "numero": "1"
                },
                "librosVendidos": [
                  "24000"
                ]
              },
              {
                "numero": {
                  "numero": "2"
                },
                "librosVendidos": [
                  "38600"
                ]
              },
              {
                "numero": {
                  "numero": "3"
                },
                "librosVendidos": [
                  "NO_INFO"
                ]
              },
              {
                "numero": {
                  "numero": "4"
                },
                "librosVendidos": [
                  "NO_INFO"
                ]
              }
            ]
          },
          {
            "zona": [
              "Centro"
            ],
            "trimestre": [
              {
                "numero": {
                  "numero": "1"
                },
                "librosVendidos": [
                  ""
                ]
              },
              {
                "numero": {
                  "numero": "2"
                },
                "librosVendidos": [
                  "16080"
                ]
              },
              {
                "numero": {
                  "numero": "3"
                },
                "librosVendidos": [
                  "25000"
                ]
              },
              {
                "numero": {
                  "numero": "4"
                },
                "librosVendidos": [
                  "29000"
                ]
              }
            ]
          },
          {
            "zona": [
              "Sur"
            ],
            "trimestre": [
              {
                "numero": {
                  "numero": "1"
                },
                "librosVendidos": [
                  "27000"
                ]
              },
              {
                "numero": {
                  "numero": "2"
                },
                "librosVendidos": [
                  "31400"
                ]
              },
              {
                "numero": {
                  "numero": "3"
                },
                "librosVendidos": [
                  "40100"
                ]
              },
              {
                "numero": {
                  "numero": "4"
                },
                "librosVendidos": [
                  "30000"
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