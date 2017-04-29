#CONTRATO:
#Problema: Determinar la facturación de materiales de contrucción (en tabla9
#Entradas: Preguntas al usuario -> "¿Cuantos materiales llevara?", "¿Cuál es el precio de cada uno?" (entero)
#Salidas: Una tabla que muestre el n articulo, el valor, el iva, el valor+iba, el precio con iva y su total
#Restricciones: Ingresar el precio y la cantidad en numeros

#Procedimiento:
#1) Preguntar al usuario cuantos materiales llevara, iniciando la suma y el contador en 0
#2) Establecer la condicion de que si los materiales son 1 o más, pregunta el precio de cda uno
#3) Para preguntar el precio de c/u materiales reducira su valor en 1
#4) Calculo el iva respectivamente multi el precio por 16 y dividido entre 100 (uso // para no mostrar parate decimal)
#5) Sumo el precio mas el iva y su resultado sera el total y el precio del articulo ( establezco variables )
#6) El contador sera igual al contador mas el valor del articulo con iva para respresentarlo en la tabla como un resultado
#7) Se organiza en el print cada variable asignada y se hace uso de "\t" para tabular.


def empresan():
    materiales= int(input("¿Cuantos materiales llevará? "))
    suma=0
    cont=a
    while materiales >= 1:
        materiales=materiales-1
        precio= int(input("¿Cuál es el precio del material? "))
        iva= precio*16//100
        valoriva= precio+iva
        total= valoriva
        suma=1+suma
        cont = cont + total
        print("\t # \t ""Valor $" "\t IVA" "\t Valor+IVA" "\t Precio Articulo \t""\n""\t",1,"\t",precio,"\t""\t", iva,"\t", valoriva,"\t""\t""$",total,"\t")
    print ("\n Total a pagar =  $" + str(cont))

empresan()
