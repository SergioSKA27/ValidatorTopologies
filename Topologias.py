from ast import main
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
        for i in elements:
            if self.elements.get(i,None) == None:
                self.elements[i] = i
    else:
        self.elements = None


# It creates a new class called Subset that inherits from the Set class.
class Subset(Set):

    def  __init__(self,elements):
        """
        The function __init__() is a constructor that initializes the class Vector

        :param elements: a list of elements
        """
        super().__init__(len(elements), elements)




S1 = Set(3, [1,2,3])



Ss1 = Subset([1])

print(type(S1))
print(Ss1.elements)






layout0 = [[sg.Text("Ingrese el conjunto a evaluar")],[sg.Input("",key='-Setinput-')]]



mainlayout =  [[sg.Column(layout0,key='-col1-',visible=True)]]
window = sg.Window(title="TOPOLOGIAS", layout=mainlayout,auto_size_buttons=True,auto_size_text=True,resizable=True)

# Create an event loop
while True:
    event, values = window.read()#Captura los eventos y los valores de los elementos
    #Evento para cerrar el programa
    if event == sg.WIN_CLOSED:
        break
