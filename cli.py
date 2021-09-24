from multiproceso import procesarListaLink
def interfaz():
    lista_links = list()
    data = " "
    while data != "salir":
        data = input("Ingrese Links ( escriba salir para salir obvio ctm, no sea weon ): ")
        if (data != "salir"):
            lista_links.append(data)

    print("Descargando...")
    procesarListaLink(lista_links)