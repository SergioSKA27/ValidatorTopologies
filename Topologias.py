
from itertools import combinations, permutations,chain
import copy
import itertools
import PySimpleGUI as sg


#Created by: Lopez Martinez Sergio Demis
#this help us to identify all the topologies in a given set

#the conditions we consider to say  a pair  of the form (T,s)
#whit T a set of subsets of s. Is given as follow

#1.the empty set belongs to T, as well as  the set s

#2.the union  of an arbitrary number of elements on T , belongs to T as well

#3.  the intersection of  any two members of T belongs to T



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
        uni = Set(0,[])

        for i in self.elemtslist:
                uni.addelement(i)
        for j in list(other.elementsscpy()):
                uni.addelement(j)

        return uni

    def Intersection(self, other):
        inter = Set(0,[])

        if self.is_emptyset() or other.is_emptyset():
            return inter

        for i in self.elemtslist:
            if other.belong(i):
                inter.addelement(i)

        return inter

    def __repr__(self) -> str:
        if self.is_emptyset():
            return "∅"
        return str(self.elements)

    def __str__(self) -> str:
        if self.is_emptyset():
            return "∅"
        ss = "{"
        for i in  self.elemtslist:
            ss = ss + str(i) + ','
        return ss + '}'

    def Powerset(self):
        Ps = []
        ts = chain.from_iterable(combinations(self.elemtslist, r) for r in range(len(self.elements)+1))
        for e in ts:
            if len(e) == 0:
                Ps.append(Set(0,[]))
            else:
                Ps.append(Set(len(e),e))
        return Ps







# It creates a new class called Subset that inherits from the Set class.
class Subset(Set):

    def  __init__(self,elements):
        """
        The function __init__() is a constructor that initializes the class Vector

        :param elements: a list of elements
        """
        super().__init__(len(elements), elements)








S1 = Set(4, [1,2,3,4])
S2 = Set(3, [5])
P = []


P = S1.Powerset()

print(S1.Intersection(S2))



print(len(P))




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



window.close() #Cerramos la ventana
