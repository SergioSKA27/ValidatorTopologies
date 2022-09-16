
from itertools import combinations, permutations,chain
from os import system
import copy
import PySimpleGUI as sg
import platform

if platform.system() == 'Linux':
    CLEARW = 'clear'
elif platform.system() ==  'Windows':
    CLEARW = 'cls'

#the number of the position i in the list is equal to the number of topologies in a set of i elements
NUMBERTOPOLOGIES = [1,1,4,29,355,6942,209527,9535241,642779354,63260289423,8977053873043,1816846038736192, 519355571065774021, 207881393656668953041, 115617051977054267807460, 88736269118586244492485121, 93411113411710039565210494095, 134137950093337880672321868725846,]


#Created by: Lopez Martinez Sergio Demis
#this help us to identify all the topologies in a given set

#the conditions we consider to say  a pair  of the form (T,s)
#whit T a set of subsets of s. Is given as follow

#1.the empty set belongs to T, as well as  the set s

#2.the union  of an arbitrary number of elements on T , belongs to T as well

#3.the intersection of  any two members of T belongs to T



# If the elements are a string, then the elements are set to None. Otherwise, the elements are set to a dictionary with
# the elements as keys and the elements as values
class Set:
    def __init__(self,size, elements):
        """
        If the elements are a string, then the elements are set to None. Otherwise, the elements are set to a dictionary with
        the elements as keys and the elements as values.

        :param size: the size of the set
        :param elements: a list of elements that are in the set
        """
        self.size = size

        if type(elements) !=  type(""):
            self.elements = {}
            if self.size > 0:
                for i in list(elements):
                    if self.elements.get(i,None) == None:
                        self.elements[i] = i
        else:
            self.elements = None

        self.elemtslist = list(self.elements)


    def belong(self,element):
        """
        It returns True if the element is in the set, and False otherwise

        :param element: The element to check for
        :return: The value of the key element.
        """
        return self.elements.get(element, None) != None

    def addelement(self,element):
        """
        It adds an element to the set.

        :param element: The element to add to the set
        """
        attr = self.elementsscpy()
        attr[element] = element
        self.elements = attr
        self.elemtslist = list(attr)

    def elementsscpy(self):
        """
        It returns a copy of the elements in the set.
        :return: A copy of the elements list.
        """
        return copy.copy(self.elements)

    def is_emptyset(self):
        """
        It checks if the set is empty.
        :return: True if the set is empty,false in other case
        """
        return len(self.elements) == 0

    def uNION(self, other):
        """
        It takes the elements of the first set and adds them to a new set, then it takes the elements of the second set and
        adds them to the new set

        :param other: Set
        :return: The union of the two sets.
        """
        uni = Set(0,[])

        for i in self.elemtslist:
                uni.addelement(i)
        for j in list(other.elementsscpy()):
                uni.addelement(j)

        return uni

    def Intersection(self, other):
        """
        It returns the intersection of two sets.

        :param other: Set
        :return: The intersection of two sets.
        """
        inter = Set(0,[])

        if self.is_emptyset() or other.is_emptyset():
            return inter

        for i in self.elemtslist:
            if other.belong(i):
                inter.addelement(i)

        return inter

    def __repr__(self) -> str:
        """
        The function returns a string representation of the set
        :return: The elements of the set.
        """
        k = 0
        if self.is_emptyset():
            return "∅"
        ss = "{"
        for i in  self.elemtslist:
            if k != len(self.elements)-1:
                ss = ss + str(i) + ','
            else:
                ss = ss + str(i)
            k += 1
        return ss + '}'

    def __str__(self) -> str:
        """
        The function takes a set and returns a string representation of the set
        """
        k = 0
        if self.is_emptyset():
            return "∅"
        ss = "{"
        for i in  self.elemtslist:
            if k != len(self.elements)-1:
                ss = ss + str(i) + ','
            else:
                ss = ss + str(i)
            k += 1
        return ss + '}'

    def __eq__(self, __o: object) -> bool:
        """
        It checks if the two sets are equal by checking if the elements of one set are in the other set and vice versa

        :param __o: object
        :type __o: object
        :return: a boolean value.
        """
        flag = True
        if not isinstance(__o,self.__class__ ):
            return False

        if len(self.elements) != len(__o.elementsscpy()):
            return False
        else:
            if len(self.elements) == 0:
                return True
            for i in self.elemtslist:
                if __o.belong(i) == False:
                    flag = False
                    break
                else:
                    continue
            if flag:
                for j in list(__o.elementsscpy()):
                    if self.belong(j) == False:
                        flag = False
                        break
                    else:
                        continue
        return flag

    def __hash__(self) -> int:
        """
        The hash function is a function that takes in an input of any size, performs an operation on it, and returns a fixed
        size output
        :return: The hash of the tuple of the elements.
        """
        return hash(tuple(sorted(self.elements.values())))

    def Powerset(self):
        """
        It returns the powerset of a set.
        :return: A list of sets.
        """
        Ps = []
        ts = chain.from_iterable(combinations(self.elemtslist, r) for r in range(len(self.elements)+1))
        for e in ts:
            if len(e) == 0:
                Ps.append(Set(0,[]))
            else:
                Ps.append(Set(len(e),e))
        return Ps

def FamilySetUnion(F) -> Set:
    U = copy.copy(F[0])
    for i in range(1,len(F)):
        U = U.uNION(F[i])
    return U

def is_topologie(T, s):
    """
    The function checks if the given set of sets is a topology on the given set.

    :param T: a list of sets
    :param s: the set of all elements
    :return: A boolean value.
    """
    whhy = []
    flag1 = 0
    for i in  T:
        if i.is_emptyset():
            #print("000")
            flag1 += 1
            break

    for i in  T:
        if i == s:
            flag1 += 1
            break

    if flag1 < 2 :
        return False


    pairs = []

    #Combinations of families Union
    flag2 = True
    for i in range(2,len(T)+1):
        cm = combinations(T,i)
        if i == 2:
            pairs = list(cm)

        for j in list(cm):
            #print("TS",j)
            FU = FamilySetUnion(j)
            #print("FU ",FU)
            blongTt = False
            for k in  T:
                if k == FU:
                    blongTt = True
            if blongTt == False:
                flag2 = False
                break

        #print("-------------")

    if(flag2 == False):
        return False

    #print(pairs)
    flag3 =  True
    for i in  range(0,len(pairs)):
        intr = pairs[i][0].Intersection(pairs[i][1])
        gg = False
        for j in T:
            if j == intr:
                gg = True
                break
        if gg == False:
            flag3 = False
            break

    if(flag3 == False):
        return False


    return True

def topologies_of_Set(S):
    """
    It takes a set S and returns a list of all the topologies of S

    :param S: The set of elements that the topology will be defined on
    """
    kk = 1

    if S.is_emptyset():
        return [(S,S)],[]
    t = []
    nt = []
    P = S.Powerset()
    for i in range(1,len(P)+1):
        perms = combinations(P,i)
        for cs in list(perms):
            if len(cs) == 1:
                nt.append(cs)
                continue
            if len(cs) == len(P):
                print(kk,"TOPOLOGY :)",cs)
                kk += 1
                t.append(cs)
                continue

            if len(cs) != len(P) and is_topologie(cs,S) :
                print(kk,"TOPOLOGY :)",cs)
                kk += 1
                t.append(cs)
            else:
                #print(cs)
                nt.append(cs)
    return t,nt


def isvalidinput(S):
    hset = False
    for i in  S:
        if i == '}' or i == '{':
            hset = True
        else:
            continue

    if not hset:
        return True
    else:
        stackk = []
        for i in S:
            if i == '{':
                stackk.append(i)
            elif i == '}':
                if stackk[len(stackk)-1] ==  '{':
                    #print(stackk[len(stackk)-1],"GG")
                    stackk.pop()
                else:
                    break
            else:
                continue
        #print(stackk)
        return len(stackk) == 0

def makeset(S):
    ss = ""
    cj = []
    stackk = []

    for i in  S:
        print("ss",ss)
        if i == '{' and i != ',' and i != '|' and i != ';' and i !=  ' ' and i != '}':
            stackk.append(i)
        elif  i != ',' and i != '|' and i != ';' and i !=  ' ' and i != '{' and i != '}':
            ss = ss + i
        elif  i == ',' or i == '|' or i == ';' or i ==  ' ' and i != '{' and i != '}' :
            stackk.append(ss)
            ss = ""
        elif i == '}' and i != ',' and i != '|' and i != ';' and i !=  ' ' and i != '{':
            ins = []
            print("SETT",stackk)
            while(len(stackk) > 0):
                if stackk[len(stackk)-1] != '{':
                    ins.append(stackk.pop())
                else:
                    break
            if len(stackk) > 0:
                stackk.append(Set(len(ins),ins))
            else:
                cj.append(Set(len(ins),ins))

    while(len(stackk) > 0):
        cj.append(stackk.pop())
    if len(ss) > 0:
        cj.append(ss)
    return Set(len(cj),cj)





def readinput(s):
    """
    It takes a string and returns a set

    :param s: the string to be read
    :return: A set of strings.
    """
    if len(s) == 0 :
        return Set(0,[])
    else:
        cset = Set(0,[])
        ss = ""
        for i in s:
            if i != ',' and i != '|' and i != ';' and i !=  ' ' and i != '{' and i != '}' :
                ss = ss + i
            elif i == '{' or i == '}':
                continue
            else :
                cset.addelement(ss)
                ss = ""


        if len(ss) != 0:
            cset.addelement(ss)
        return cset

def whyis_topologie(T, s):
    """
    The function checks if the given set of sets is a topology on the given set.

    :param T: a list of sets
    :param s: the set of all elements
    :return: A boolean value.
    """
    whhy = []
    flag1 = 0
    for i in  T:
        if i.is_emptyset():
            #print("000")
            flag1 += 1
            break

    for i in  T:
        if i == s:
            flag1 += 1
            break

    if flag1 < 2 :
        print("1) ",str(Set(0,[])),",", s,"¬(E) τ.")
        return False


    print("1) ",str(Set(0,[])),",", s,"E τ.")
    print("---------------------------------------------")



    #Combinations of families Union
    print("2) La union de todas la posibles familias de conjuntos de τ")
    flag2 = True
    for i in range(2,len(T)+1):
        cm = combinations(T,i)
        #print("Colecciones de Tamaño", i)
        #print(list(cm))

        for j in list(cm):
            print("U",j)
            FU = FamilySetUnion(j)
            blongTt = False
            for k in  T:
                if k == FU:
                    #print(FU,"∈ τ.")
                    blongTt = True
            if blongTt == False:
                #print(FU,"¬(∈) τ.")
                flag2 = False
                break

        #print("-------------")

    if(flag2 == False):
        print("¬(E) τ.")
        return False
    else:
        print("E τ.")

    print("---------------------------------------------")
    pairs = list(combinations(T,2))
    print("3) La intersección de todos los posibles pares de elementos de τ")
    flag3 =  True
    for i in  range(0,len((pairs))):
        print(pairs[i][0],"n",pairs[i][1])
        intr = pairs[i][0].Intersection(pairs[i][1])
        gg = False
        for j in T:
            if j == intr:
                gg = True
                break
        if gg == False:
            flag3 = False
            break

    if(flag3 == False):
        print("¬(E) τ.")
        return False

    print("E τ.")
    return True

#S1 = Set(2, [Set(2,[1,2]),Set(1,[Set(1,[666])]),Set(0,[]),Set(0,[])])
#print(S1)
#print(isvalidinput("{{{{}}}"))
#st = "{1,2,3},{},{2,666},5"

#stt = makeset(st)

#print(stt)
"""
    Los pasos que seguimos para obtener las topologías de un conjunto finito de elementos son los siguientes :

    1)Obtenemos el conjunto potencia del conjunto dado.

    2)Una vez tenemos el conjunto potencia, procederemos a calcular todas las posibles combinaciones de elementos tomados
    en conjuntos de tamaño 2,... hasta n, de elementos del conjunto potencia.

    3) Con cada conjunto de combinaciones comprobamos cuales de ellas, cumplen las caracteristicas de una Topología

        3.1)Verificamos que el conjunto original y el conjunto vacío pertenescan a la Topología

        3.2)Calculamos todas las posibles combinaciones de elementos(tomados en conjuntos de 2 hasta n) de la topología y verificamos que la unión arbitraria de cualquier numero de elementos pertenezca a la topología

        3.3)Calculamos todas las posibles combinaciones de elementos tomados en conjuntos de 2 y verificamos que la intersección pertenezca a la topología

    4)Retornamos una lista con las topologias validas y otra con aquellas que no lo son.
"""

#GUI Part

sg.theme('Dark Blue 3')


#Some text for the Help Section :)

TextFuncApp0 = "La aplicaión fue diseñada para Calcular  todas las posibles topologías de un conjuto(finito) dado , además de proporcionar todas aquellas que no lo son. "
TextFuncApp1 = "El funcionamiento de la aplicación en bastante sencillo , en el apartado principal podra encontrar tres diferentes elementos, tales como una caja de texto en la cual podra ingresar el conjunto deseado, separando los elementos del conjunto por alguno de los siguientes simbolos: \n"
TextFuncApp2 = "Simbolos Separadores : coma, ;, |, espacio.\n No existe ninguna restricción para definir los miembros del conjunto por tanto cualquier elemento que pueda ser representado por medio de caracteres ASSCI es valido.\n A continuacion Algunos ejemplos de conjutos:  \n"
TextFuncApp3 = "El conjunto {A,B,C} deberia de ingresarse como A,B,C o A;B;C o A B C o A|B|C.\n El conjunto {1,2,3} debería de ingresarse como 1,2,3 o 1;2;3 o 1 2 3 o 1|2|3.\n"
TextFuncApp4 = "Finalmente debería presionar el boton de calcular topolpogías, el cual lo dirigira a la seccion donde podra consular aquellas que si lo son y aquellas que no lo son.\n En caso de necesitar ayuda simpre podra presionar el boton ayuda ubicado en la pantalla inicial, y consultar cualquiera de los apartados de dicha sección."
TextFuncApp = TextFuncApp0 + TextFuncApp1 + TextFuncApp2 +TextFuncApp3 +TextFuncApp4
textytopology0 = "La Topología es una generalización de algunas de las propiedades de intervalo abierto en la recta real, propiedades independientes de otras presentes en R como la suma, el orden o la distancia.\n"
textytopology1 = "Definición\n Una topología sobre un conjunto X, es una familia τ ⊂ P(X), verificando \n(i) ∅, X ∈ τ ,\n(ii) si A, B ∈ τ , entonces A ∩ B ∈ τ ,\niii) si { A_i } , i∈I ⊂ τ , entonces ∪ A_i ∈ τ.\nLos elementos de τ se llaman abiertos y el par (X, τ ) se llama espacio topológico."
textytopology2 ="\nEjemplos\n Se introducen algunos ejemplos fundamentales en topología \n1) sobre X, τind = {∅, X} es la topología indiscreta;\n2) sobre X, τdis = P(X) es la topología discreta;"
textytopology3 = "\n\n\nNúmero de topologías en un conjunto finito\n Las topologías en un conjunto finito tienen una correspondencia uno a uno con los preordenes en el conjunto, y las topologías T0 tienen una correspondencia uno a uno con los ordenes parciales. Por lo tanto, el número de topologías en un conjunto finito es igual al número de preordenes y el número de topologías T0 es igual al número de ordenes parciales."
textytopology4 = "\nSea T(n) el número de topologías distintas en un conjunto con n puntos. No existe una fórmula simple conocida para calcular T(n) para n arbitrario. La Enciclopedia en línea de secuencias enteras actualmente enumera T (n) para n ≤ 18.\nEl número de topologías T0 distintas en un conjunto con n puntos, denotado T0(n), está relacionado con T(n) por la fórmula \n\n T(n) = Σ (S(n,k)*T0(k)), 0 ≤ k ≤ n\n\n"
textytopology5 = "donde S(n,k) denota el número de Stirling de segunda clase.\n(En matemáticas, particularmente en combinatoria, un número de Stirling del segundo tipo (o número de partición de Stirling) es el número de formas de dividir un conjunto de n objetos en k subconjuntos no vacíos y se denota por S ( n , k ).)"
textytopology6 = "\nLa siguiente tabla enumera el número de topologías distintas (T0) en un conjunto con n elementos. También enumera el número de topologías no equivalentes (es decir, no homeomorfas)."
textytopology = textytopology0 +textytopology1 + textytopology2 +textytopology3 +textytopology4+textytopology5+textytopology6
#Layout 0 (First)
textalgorithm = """
    Los pasos que seguimos para obtener las topologías de un conjunto finito de elementos son los siguientes:

    1)Obtenemos el conjunto potencia del conjunto dado.

    2)Una vez tenemos el conjunto potencia, procederemos a calcular todas las posibles combinaciones de elementos tomados
    en conjuntos de tamaño 2,... hasta n, de elementos del conjunto potencia.

    3) Con cada conjunto de combinaciones comprobamos cuales de ellas, cumplen las caracteristicas de una Topología

        3.1)Verificamos que el conjunto original y el conjunto vacío pertenescan a la Topología

        3.2)Calculamos todas las posibles combinaciones de elementos(tomados en conjuntos de 2 hasta n) de la topología y verificamos que la unión arbitraria de cualquier numero de elementos pertenezca a la topología

        3.3)Calculamos todas las posibles combinaciones de elementos tomados en conjuntos de 2 y verificamos que la intersección pertenezca a la topología

    4)Retornamos una lista con las topologias validas y otra con aquellas que no lo son.
"""
layout0 = [[sg.Button("Ayuda?",key='-Bhelp-')],[sg.Text("Ingrese el conjunto a evaluar")],[sg.Input("",key='-Setinput-')],
            [sg.Button("Calcular Topologias",key='-Btopologies-')]]

#Layout 1 (help)
layout1 = [[sg.Button("<-",key='-returnL0-')],[sg.Button("Funcionamiento de la Aplicacion", key='-Bfunc-')],
            [sg.Button("Topologias",key='-btopologiesfunc-')],[sg.Button("Algortimo Empleado",key='-Balgorithm-')]]

#layout 2 (How to use the app)
layout2 = [[sg.Button("<-",key='-returnL1L2-')],[sg.Text("Funcionamiento de la aplicacion")],
            [sg.Multiline(TextFuncApp,key='-Funcapp-',size=(50,8),disabled=True)]]
#Layout 3 (Information about Topologies)
layout3 = [[sg.Button("<-",key='-returnL1L3-')],[sg.Text("Informacion acerca de Topologias ")],
            [sg.Multiline(textytopology,key='-Topoinfo-',size=(50,8),disabled=True)],[sg.Image('Table1.png',key='-img1-')]]

#Layout 4 (topologies , No topologies and Power Set)
layout4 = [[sg.Button("<-",key='-returnL0L4-')],[sg.Text("Topologías y No topologías del conjunto")],[sg.Text("∅",key='-Setstr-')],[sg.Button("Conjunto Potencia", key='-Bpowerset-')],
            [sg.Button("Topologías", key='-Btopologias-')],[sg.Button("No topologías", key='-BNtopologias-')]]

#Layout 5(Power SetTable)
layout5 = [[sg.Button("<-",key='-returnL4L5-')],[sg.Text("Tabla del conjunto Potencia ")],
            [sg.Table([[]],max_col_width=50,key='-powersetTable-',headings=["Subconjuntos"], hide_vertical_scroll=False, vertical_scroll_only=False,
            auto_size_columns=False,col_widths=[100,50],justification='left')]]

#Layout 6(Topologies Set Table)
layout6 = [[sg.Button("<-",key='-returnL4L6-')],[sg.Text("Tabla de Topologías")],
            [sg.Table([[]],key='-topologiesTable-',headings=["Topologías"], hide_vertical_scroll=False, vertical_scroll_only=False,
            auto_size_columns=False,col_widths=[100,50],justification='left')],[sg.Button("Why?",key='-whyistopology-')]]

#Layout 7(No Topologies Set Table)
layout7 = [[sg.Button("<-",key='-returnL4L7-')],[sg.Text("Tabla de No Topologías")],
            [sg.Table([[]],key='-notopologiesTable-',headings=["No Topologías"], hide_vertical_scroll=False, vertical_scroll_only=False,
            auto_size_columns=False,col_widths=[100,50],justification='left')],[sg.Button("Why?",key='-whyisnotopology-')]]
#layout 8 (How the algorithm works)
layout8 = [[sg.Button("<-",key='-returnL1L8-')],[sg.Text("Funcionamiento del algoritmo")],
            [sg.Multiline(textalgorithm,key='-Funcalgo-',size=(50,8),disabled=True)]]


#Main layout
mainlayout =  [[sg.Column(layout0,key='-col1-',visible=True),sg.Column(layout1,key='-col2-',visible=False),sg.Column(layout2,key='-col3-',visible=False),
                sg.Column(layout3,key='-col4-',visible=False),sg.Column(layout4,key='-col5-',visible=False),sg.Column(layout5,key='-col6-',visible=False),
                sg.Column(layout6,key='-col7-',visible=False),sg.Column(layout7,key='-col8-',visible=False),sg.Column(layout8,key='-col9-',visible=False)]]
window = sg.Window(title="TOPOLOGIAS", layout=mainlayout,auto_size_buttons=True,auto_size_text=True,resizable=True)

sg.popup("Le recomendamos dar un vistazo al apartado de ayuda ubicado en la parte superior de la pantalla, antes de comenzar a usar la aplicación")
# Create an event loop
while True:
    event, values = window.read()#Captura los eventos y los valores de los elementos
    #print(event)
    #print(values)
    #Evento para cerrar el programa
    if event == sg.WIN_CLOSED:
        break

    if event == '-Bhelp-':
        window['-col1-'].update(visible=False)
        window['-col2-'].update(visible=True)

    if event == '-Bfunc-':
        window['-col2-'].update(visible=False)
        window['-col3-'].update(visible=True)

    if event == '-btopologiesfunc-':
        window['-col2-'].update(visible=False)
        window['-col4-'].update(visible=True)

    if event == '-Balgorithm-':
        window['-col2-'].update(visible=False)
        window['-col9-'].update(visible=True)

    if event == '-Btopologies-':
        system(CLEARW)
        iset = readinput(values['-Setinput-']) #Original Set

        if(len(iset.elementsscpy()) > 3):
            longi = len(iset.elementsscpy())
            if longi > 18:
                #Your PC can go fire :V
                longi = "Are you crazy?(Inf)"
            else:
                longi = NUMBERTOPOLOGIES[longi]
            clicked = sg.PopupOKCancel("El numero de elementos que ingreso es mayor a 3,el calculo tomara un tiempo por favor espere :)","Numero de elementos a calcular: " + str(longi),title="Tiempo de Calculo")
        else:
            clicked = None
        if clicked == 'Cancel':
            continue
        else:
            Piset = iset.Powerset() #Power Set
            t,nt = topologies_of_Set(iset) #
            ttop = []
            nttop = []
            #print(t[0])

            for i in  t:
                #print(i)
                ttop.append([str(i)])

            for i in  nt:
                #print(i)
                nttop.append([str(i)])

            #print(iset)
            #system("cls")
            window['-powersetTable-'].update(values=Piset)
            window['-topologiesTable-'].update(values=ttop)
            window['-notopologiesTable-'].update(values=nttop)
            window['-Setstr-'].update(value=iset)
            window['-col1-'].update(visible=False)
            window['-col5-'].update(visible=True)

    if event == '-Bpowerset-':
        window['-col5-'].update(visible=False)
        window['-col6-'].update(visible=True)

    if event == '-Btopologias-':
        window['-col5-'].update(visible=False)
        window['-col7-'].update(visible=True)

    if event == '-BNtopologias-':
        window['-col5-'].update(visible=False)
        window['-col8-'].update(visible=True)

    if event == '-whyistopology-' and len(values['-topologiesTable-']) > 0:
        #print((values['-topologiesTable-'][0]))
        system(CLEARW)
        whyis_topologie(t[values['-topologiesTable-'][0]],iset)

    if event == '-whyisnotopology-' and len(values['-notopologiesTable-']) > 0:
        #print((values['-notopologiesTable-'][0]))
        system(CLEARW)
        whyis_topologie(nt[values['-notopologiesTable-'][0]],iset)



    if event == '-returnL0-':
        window['-col1-'].update(visible=True)
        window['-col2-'].update(visible=False)

    if event == '-returnL0L4-':
        window['-col1-'].update(visible=True)
        window['-col5-'].update(visible=False)
        window['-Setinput-'].update(value="")

    if event == '-returnL1L2-' and window['-col3-'].visible == True:
        window['-col2-'].update(visible=True)
        window['-col3-'].update(visible=False)

    if event == '-returnL1L3-' and window['-col4-'].visible == True:
        window['-col2-'].update(visible=True)
        window['-col4-'].update(visible=False)

    if event == '-returnL1L8-' and window['-col9-'].visible == True:
        window['-col2-'].update(visible=True)
        window['-col9-'].update(visible=False)


    if event == '-returnL4L5-' and window['-col6-'].visible == True:
        window['-col5-'].update(visible=True)
        window['-col6-'].update(visible=False)

    if event == '-returnL4L6-' and window['-col7-'].visible == True:
        window['-col5-'].update(visible=True)
        window['-col7-'].update(visible=False)

    if event == '-returnL4L7-' and window['-col8-'].visible == True:
        window['-col5-'].update(visible=True)
        window['-col8-'].update(visible=False)






window.close() #Cerramos la ventana
