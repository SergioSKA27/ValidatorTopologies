# ValidatorTopologies

(**Por alguna razon Windows lo detecta como virus :( , puede revisar el codigo y cerciorarse de que no lo es)


Una aplicacion simple que evalua las topologias en un conjunto finito de elementos :)

Dentro de la aplicación  puede ingresar el conjunto que desee separando los elementos por una coma o espacio. Posteriormente debe dar click al botón calcular topologías, en caso de que el número de elementos en el conjunto sea mayor que 3 el proceso puede demorar un poco y la ventana de la aplicación puede presentar el mensaje de no responde, esto es porque la interfaz gráfica espera a que el cálculo se termine de realizar para poder pasar al siguiente menú, en cualquier caso si desea ver el proceso las topologías que se vayan encontrando aparecerán en la segunda pantalla de terminal, indicando cuantas topologías se han calculado hasta el momento, una vez terminado este proceso pasará a la ventana donde podrá visualizar una tabla con todas las topologías además de una tabla con el conjunto potencia y  las no topologías. En el apartado de las tablas de topologías y no topologías podrá seleccionar cualquier elemento de la tabla dando click sobre el elemento y podrá presionar el botón 'Why?' que le mostrará el porqué dicho elemento es una topología en la pantalla de terminal, para regresar a cualquiera de los menús anteriores podrá presionar la flecha (<-) que se encuentra en la parte superior izquierda de la pantalla. Puede probar cualquier conjunto que desee sin necesidad de cerrar el programa solo presione la flecha hasta regresar el menú principal e ingrese el nuevo conjunto.


#Update 

Ahora podemos Trabajar con conjuntos cuyos elementos sean unicamente conjuntos, siempre y cuando no tengan conjuntos anidados, algunos ejemplos de como ingresar este tipo de conjuntos:

 {{1,2,3},{4,5},{6}} se escribe como {1,2,3},{4,5},{6}
 
 el conjunto vacío se escribe como {}
 
 Nota: Los conjuntos no pueden contener conjutos y elementos simples mezclados, es decir los conjuntos deben ser de un mismo tipo con todos sus elementos conjuntos o todos sus elementos objetos simples, ejemplo:
 
 El conjunto {1,{1}} no es valido dado que 1 es simple y {1} es un conjunto. De igual forma {1,{2}} tampoco es valido dado que el conjunto {2} se encuentra anidado detro del conjunto {1,{2}}.
