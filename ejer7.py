import time
import os
try:
    listaConfirmados=[414, 719, 821, 262, 1030, 567, 523, 886, 192, 5414]
    listaNuevos=[33, 46, 95, 42, 148, 64, 92, 79, 24, 623]
    listaProvincia=['Ávila', 'Buergos', 'León', 'Palencia', 'Salamanca', 'Soria', 'Valladolid', 'Zamora', 'Castilla y Leon']
    inicio="inicio"
    def opcion1(listaProvincia, listaConfirmados, listaNuevos): 
            #Dar de alta  Provincia y datos (confirmados y nuevos)
        provincia=input("Provincia: ")
        confirmados=int(input("Número de confirmados dados de alta: "))
        nuevos=int(input("Número de nuevos: "))
        if provincia in listaProvincia:
            posicion=listaProvincia.index(provincia) #buscar la poscion de la provincia introducida
            nuevosConfirmados=listaConfirmados[posicion] #obtengo el elemento por medio de la posicion
            resultado=nuevosConfirmados-confirmados#rsto el elemento obtnido por los dado de alta introducido por teclado
            nuevosNuevos=listaNuevos[posicion]
            resultadoN=nuevosNuevos-nuevos
            print("Dados de alta en confirmados: ",nuevosConfirmados,"Dados de alta en nuevos:",nuevosNuevos)
            print("Actuales confirmados: ",resultado,"Actuales en nuevos:",resultadoN)
                
        
        else:
            print("a provincia introducida no se encuentra en la lista.")
        input("\nPulse cualquier tecla para continuar...")
        return listaProvincia, listaConfirmados, listaNuevos
        
    def opcion2(listaConfirmados, listaNuevos):
        #Introduce una provincia para modificar sus datos(confirmados y nuevos
        provincia=input("Introduce la provincia a modificar: ")             
        if provincia in listaProvincia: #si la provincia que he puesto esta en su lista
            confirmados=int(input("Modificacion del nº de confirmados: "))
            nuevos=int(input("Modificacion del nº de nuevos positivos: "))
            posicionProvincia=listaProvincia.index(provincia) #busco la posicion de la provincia que he introducido
            listaConfirmados[posicionProvincia]=confirmados #La posicion de la provincia que he puesto antes tendra en la lista confirmados lso datosque hacen referencia ha dicha posicion, entonces ahora cambio la los nuevos confirmados segun la posicion 
            listaNuevos[posicionProvincia]=nuevos
            print("Confirmados: ",listaConfirmados[posicionProvincia], "Nuevos: ",listaNuevos[posicionProvincia])
        else: 
            print("La provincia introducida no esta en la lista.")
            input("\nPulse cualquier tecla para continuar...")
            return listaConfirmados, listaNuevos            
            
    
    def opcion3_lista(listaProvincia):
            #Numero Total de casos Confirmados en la Comunidad
        provincia=input("Provincia: ")           
        if provincia in listaProvincia:
            posicion=listaProvincia.index(provincia)
            print("Confirmados: ",listaConfirmados[posicion], "Nuevos: ",listaNuevos[posicion])
        else:
            print("La provincia introducida no esta en la lista.")
        input("\nPulse cualquier tecla para continuar...")
        return listaConfirmados, listaNuevos           
        
            
    def opcion4(listaProvincia,listaConfirmados,listaNuevos):
            #Listado de la situacion  general por provincias(confirmados y nuevos)
        for x in range(len(listaConfirmados)):
            print(listaProvincia[x],listaConfirmados[x],listaNuevos[x]) 
        input("\nPulse cualquier tecla para continuar...")  
        return listaProvincia,listaConfirmados,listaNuevos
                        

    while inicio=="inicio":
        #os.system ("cls")  
        print("Situación epidemiológica del coronavirus (COVID-19) en Castilla y León ")
        #print ("Actualización diaria. Datos a ",time.strftime("%d/%m/%y"))
        print("\t1.- Dar de alta  Provincia y datos (confirmados y nuevos)")
        print("\t2.- Introduce una provincia para modificar sus datos(confirmados y nuevos) " )
        print("\t3.- Numero Total de casos Confirmados y Nuevos en la Comunidad ")
        print("\t4.- Listado de la situacion  general por provincias(confirmados y nuevos)")        
        print("\t5.-Salir")
        opcion=int(input("Elige una opcion: "))
            #opciones
        if opcion==1:
            opcion1(listaProvincia, listaConfirmados, listaNuevos)
            continue        
        elif opcion==2:
            opcion2(listaConfirmados, listaNuevos)
            continue        
        elif opcion==3:
            opcion3_lista(listaProvincia)
            continue
        elif opcion==4:
            opcion4(listaProvincia,listaConfirmados,listaNuevos)
            continue        
        elif opcion==5:
            break
        elif opcion<=0:
            print("Porfavor elige una de las opciones [ 1 - 5 ]: ")
            continue
        else:
            print("Porfavor elige una de las opciones [ 1 - 5 ]: ")
            continue


        
except ValueError:
    print("No pude convertir el dato a un entero.")
except Exception as e: # OJO SIEMPRE LA ULTIMA
    print("Ha ocurrido un error no previsto del tipo ", type(e).__name__ )

