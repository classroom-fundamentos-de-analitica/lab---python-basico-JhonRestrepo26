"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
#Data preparation
x=open("data.csv","r").readlines()    #Lee
x = [z.replace("\n", "") for z in x]        #Quita retorno de carro
x = [z.replace("\t", ",") for z in x]       #Separa por columnas
x = [z.split(",") for z in x]               #Enlistado de listas
#Convirtiendo columna 4 en lista y la 5 en diccionario, para facilitar manipulación...
for j in range(len(x)):
  letras=[]
  numeros=[]
  for i in x[j]:
    if ":" in i:
      index=x[j].index(i)
      xd=x[j][3:index]
      semi_list=x[j][index:]
      semi_list=tuple(iter(semi_list))                              #paso el dic a tupla
      prueba=",".join(iter(semi_list)).replace(":",",").split(",")  #paso tupla a string, reemplazo : por , y convierto cada elemento en elementos de una lista
      for k in prueba:
        if k.isdigit():
          numeros.append(k)
        else:
          letras.append(k)
      dic={letras[l]:int(numeros[l]) for l in range(len(letras))}
      del x[j][3:]
      x[j].insert(4,dic)
      x[j].insert(3,xd)                                             #Note que x es la base de datos, estructurada


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sum=0
    for i in x:
        sum+=int(i[1])
    return sum


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
    letters=[]
    for letter in x:
        if letter[0] not in letters:
            letters.append(letter[0])
    letters.sort()
    counts=[]
    for i in letters:
        count_aux=0
        for j in x:
            if j[0]==i:
                count_aux+=1
        counts.append(count_aux)
    
    return [(letters[i] ,counts[i] ) for i in range(len(letters))]

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    letters=[]
    for letter in x:
        if letter[0] not in letters:
            letters.append(letter[0])
    letters.sort()
    counts=[]
    for i in letters:
        count_aux=0
        for j in x:
            if j[0]==i:
                count_aux+=int(j[1])
        counts.append(count_aux)
    
    zipped = zip(letters, counts)
    answer3=[*zipped]
    return answer3    
    
def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    dates=[z[2].split("-") for z in x]
    months=[]
    for date in dates:
        if date[1] not in months:
            months.append(date[1])
    months.sort()
    
    counts=[]
    for i in months:
        count_aux=0
        for j in dates:
            if j[1]==i:
                count_aux+=1
        counts.append(count_aux)
    
    zipped = zip(months, counts)
    answer4=[*zipped]
    return answer4


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    letters=[]
    for letter in x:
        if letter[0] not in letters:
            letters.append(letter[0])
    letters.sort()
    
    major=[]
    fewer=[]
    for i in letters:
        aux=[]
        for j in x:
            if j[0]==i:
                aux.append(j[1])
        major.append(int(max(aux)))
        fewer.append(int(min(aux)))
    
    zipped=zip(letters,major,fewer)
    answer5=[*zipped] 
    
    return answer5


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    keys=[]
    fewer=[]
    major=[]

    for i in x:
      for j in i[4].keys():
        if j not in keys:
          keys.append(j)
    keys=sorted(keys)

    for i in keys:
      aux=[]
      for j in x:
        if i in j[4]:
          aux.append(j[4][i])
      fewer.append(int(min(aux)))
      major.append(int(max(aux)))

    zipped=zip(keys,fewer,major)
    answer6=[*zipped]
    
    return answer6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    numbers=[]

    for i in x:
      if int(i[1]) not in numbers:
        numbers.append(int(i[1]))
    numbers=sorted(numbers)

    set_letters=[]

    for i in numbers:
      aux=[]
      for j in x:
        if i==int(j[1]):
          aux.append(j[0])
      set_letters.append(aux)
    set_letters

    zipped=zip(numbers,set_letters)
    answer7=[*zipped]
    
    return answer7


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    numbers=[]

    for i in x:
      if int(i[1]) not in numbers:
        numbers.append(int(i[1]))
    numbers=sorted(numbers)

    set_letters=[]

    for i in numbers:
      aux=[]
      for j in x:
        if i==int(j[1]):
          if j[0] not in aux:
            aux.append(j[0])
      aux.sort(key=str)
      set_letters.append(aux)

    zipped=zip(numbers,set_letters)
    answer8=[*zipped]
    
    return answer8


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    keys=[]

    for i in x:
      for j in i[4].keys():
        if j not in keys:
          keys.append(j)
    keys=sorted(keys)

    value_count=[]
    for i in keys:
      count=0
      for j in x:
        if i in j[4]:
          count+=1
      value_count.append(count)

    answer9={keys[i]:value_count[i] for i in range(len(value_count))}
    
    return answer9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    col1=[i[0] for i in x]
    col4=[len(i[3]) for i in x]
    col5=[len(i[4]) for i in x]
    zipped=zip(col1,col4,col5)
    answer10=[*zipped]
    
    return answer10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    letters=[]
    for row in x:
      for i in row[3]:
        if i not in letters:
            letters.append(i)
    letters.sort()

    count_list=[]
    for i in letters:
      count=0
      for j in x:
        if i in j[3]:
          count+=int(j[1])
      count_list.append(count)

    answer11={letters[i]:count_list[i] for i in range(len(letters))}
    
    return answer11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    letters=[]
    for row in x:
      for i in row[0]:
        if i not in letters:
            letters.append(i)
    letters.sort()

    count_value=[]
    for i in letters:
      count=0
      for j in x:
        if i==j[0]:
          for k in j[4]:
            count+=int(j[4][k])
      count_value.append(count)

    answer12={letters[i]:count_value[i] for i in range(len(letters))}
    
    return answer12
