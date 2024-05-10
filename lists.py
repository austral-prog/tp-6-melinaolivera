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
