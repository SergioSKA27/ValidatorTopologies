
from itertools import combinations, permutations,chain
import copy
import PySimpleGUI as sg


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
        if self.is_emptyset():
            return "∅"
        return str(self.elements)

    def __str__(self) -> str:
        """
        The function takes a set and returns a string representation of the set
        """
        if self.is_emptyset():
            return "∅"
        ss = "{"
        for i in  self.elemtslist:
            ss = ss + str(i) + ','
        return ss + '}'

    def __eq__(self, __o: object) -> bool:
        """
        It checks if the two sets are equal by checking if the elements of one set are in the other set and vice versa

        :param __o: object
        :type __o: object
        :return: a boolean value.
        """
        flag = True
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
    T = []
    NT = []
    P = S.Powerset()
    for i in range(1,len(P)+1):
        perms = combinations(P,i)
        for cs in list(perms):
            if len(cs) == 1:
                NT.append(cs)
                continue
            if is_topologie(cs,S):
                print("TOPOLOGY :)",cs)
                T.append(cs)
            else:
                #print(cs)
                NT.append(cs)
    #print("Tops" ,T)
    #print("NoTops",NT)




S1 = Set(2, [1,2])
Sp = Set(3, [1,2,3])
S2 = Set(4, ["A","B","C","D"])
P = []
P2 = []

topologies_of_Set(S2)



print(S1 == Sp)


"""

layout0 = [[sg.Button("Ayuda?",key='-Bhelp-')],[sg.Text("Ingrese el conjunto a evaluar")],[sg.Input("",key='-Setinput-')],
            [sg.Button("Calcular Topologias",key='-Btopologies-')]]



mainlayout =  [[sg.Column(layout0,key='-col1-',visible=True)]]
window = sg.Window(title="TOPOLOGIAS", layout=mainlayout,auto_size_buttons=True,auto_size_text=True,resizable=True)

# Create an event loop
while True:
    event, values = window.read()#Captura los eventos y los valores de los elementos
    #Evento para cerrar el programa
    if event == sg.WIN_CLOSED:
        break



window.close() #Cerramos la ventana"""
