#############################################################
# Data Structures                                           #
# Stack by: SebastianSwash                                  #
# 30/06/2018                                                #
#############################################################

class Node:

    def __init__(self,value):

        self.value = value
        self.nextn = None

    def set_value(self,value):

        self.value = value

    def get_value(self):

        return self.value

    def set_nextn(self,nextn):

        self.nextn = nextn

    def get_nextn(self):

        return self.nextn

class Stack:

    def __init__(self):

        self.top = None
        self.length = 0

    def set_top(self,top):

        self.top = top

    def get_top(self):

        return self.top

    def push(self,value):

        if self.top is None:

            self.top = Node(value)

        else:

            node = Node(value)
            node.nextn = self.top
            self.top = node

        self.length += 1

    def pop(self): #removes and returns the top value 

        if self.top is not None:

            if self.top.nextn is None:

                aux = self.top.get_value()
                self.top = None

            else:

                aux = self.top.get_value()
                self.top = self.top.nextn

            self.length -= 1    
            return aux

    def peek(self): #returns the top value (without removing)

        if self.top is not None:

            return self.top.get_value()

    def clear(self): #removes all elements

        self.top = None
        self.length = 0

    def contains(self,element_type): #Returns true if stack contains the element type (str,int,float,...) 

        if self.top is None:

            return False

        else:

            aux = self.top

            while True:

                if type(aux.get_value()) is element_type:

                    return True

                if aux.nextn is None:

                    return False

                aux = aux.nextn

    def printstack(self):

        if self.top is not None:

            aux = self.top

            while True:

                print(aux.get_value())

                if aux.nextn is None:
                    break

                aux = aux.nextn
