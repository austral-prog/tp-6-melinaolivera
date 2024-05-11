
def remove_elements(lista):
    if len(lista) >=6:
        del lista[5]
        del lista[4]
        del lista[0]
    elif len(lista) >=5:
        del lista[0]
        del lista[4]
    else:
        del lista[0]
    print(lista)

remove_elements(['red','green','white','black','pink','yellow'])

def add_elements(lista):
    lista.insert (0,'pink')
    lista.append('yellow')
    print(lista)
lista2= ['red','green','white','black']
add_elements(lista2)

def is_empty(lista):
    if len(lista) == 0:
        return "esta vacia"
    else:
        return "no esta vacia"
    lista3=[ ]
    print(is_empty(lista3))

    def check_list(lista1, lista2):
        if len(lista1)<3 or len(lista2)<3:
            return false
        else:
            return lista1[2] == lista2[2]
        lista1= ['black','pink','yellow','red','green','white']
        lista2 = ['red','green','yellow','white','black','pink']
        result= check_list(lista1, lista2)
        print(f"Expected output: {result}")
        lista3= ['black','pink','green','white']
        lista4= ['red','green','yellow','black','pink']
        result2= check_list(lista3, lista4)
        print(f"Expected output: {result2}")


def list_of_lists(listas):
    resultado= [ ]
    resultado.append(listas[0][ :2])
    resultado.append(listas[1][1:4])
    resultado.append(listas[2][-2: ])
    return resultado
sample_list= [[1,2,3],[4,5,6,7,8],[9,10,11,12]]
print(list_of_lists(sample_list))
