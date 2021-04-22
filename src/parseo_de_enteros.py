#PARSEO DE ENTEROS

string = input("Ingrese un string a convertir en entero: ")

def to_integer(string):
  if prefijo(string) == '0x':
    return es_hexa_valido(string)
  elif prefijo(string) == '0b':
    return es_binario_valido(string)
  elif prefijo(string) == '0o':
    return es_octal_valido(string)
  else:
    return es_decimal_valido(string)

def prefijo(string):
  return string[0:2]

    
def es_hexa_valido(string):
    try:
      valor = int(string,16)
      return valor
    except:
      return None

def es_octal_valido(string):
    try:
      valor = int(string,8)
      return valor
    except:
      return None

def es_binario_valido(string):
  try:
      valor = int(string,2)
      return valor
  except:
      return None

def es_decimal_valido(numero):
  try:
    valor = int(string,10)
    return valor
  except:
    return None #Si no es un entero decimal valido, entonces el string contiene algun caracter no valido.

print(to_integer(string))