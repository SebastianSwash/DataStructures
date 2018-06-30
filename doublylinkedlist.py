#############################################################
# Data Structures                                           #
# Doubly linked list by: SebastianSwash                     #
#############################################################

class Node:

    def __init__(self,value):

        self.value = value
        self.nextn = None
        self.backn = None
        self.index = 0

    def set_value(self,value):

        self.value = value

    def get_value(self):

        return self.value

    def set_nextn(self,nextn):

        self.nextn = next

    def get_nextn(self):

        return self.nextn

    def set_index(self,index):

        self.index = index

    def get_index(self):

        return self.index


class List: #Doubly Linked list

    def __init__(self):

        self.first = None
        self.last = None
        self.length = 0

    def set_first(self,first):

        self.first = first

    def get_first(self):

        return self.first

    def set_last(self,last):

        self.last = last

    def get_last(self):

        return self.last

    def checkempty(self):

        if self.first == None:

            return True

        else:

            return False    

    def pushback(self,value):

        node = Node(value)

        if self.checkempty():

            self.first = self.last = node

        else:

            node.backn = self.last
            self.last.nextn = node
            self.last = node

        self.length += 1
        self.updateindex()    

    def pushfront(self,value):

        node = Node(value)

        if self.checkempty():

            self.first = self.last = node

        else:

            node.nextn = self.first
            self.first.backn = node
            self.first = node 

        self.length += 1
        self.updateindex()    


    def popback(self):

        if self.checkempty() is not True:

            if self.first == self.last:

                self.first = self.last = None

            else:

                self.last = self.last.backn
                self.last.nextn = None

            self.length -= 1
            self.updateindex()    



    def popfront(self):

        if self.checkempty() is not True:

            if self.first == self.last:

                self.first = self.last = None

            else:

                self.first = self.first.nextn
                self.first.backn = None  

            self.length -= 1
            self.updateindex()

    def remove(self,value):

        if self.checkempty() is not True:

            if self.first.get_value() == value:

                self.popfront()

            elif self.last.get_value() == value:

                self.popback()

            else:

                aux = self.first

                while True:

                    if aux.get_value() == value:

                        aux.backn.nextn = aux.nextn
                        aux.nextn.backn = aux.backn

                        self.updatelength()
                        self.updateindex()
                        break

                    if aux == self.last:

                        break

                    aux = aux.nextn                    

    def updatelength(self):

        self.length = 0

        if self.checkempty() is not True:

            aux = self.first

            while True:

                self.length += 1

                if aux == self.last:
                    break

                aux = aux.nextn    

    def updateindex(self):

        if self.checkempty() is not True:

            index = 0
            aux = self.first
            
            while True:

                aux.set_index(index)

                if aux == self.last:

                    break

                aux = aux.nextn
                index += 1

    def printlist(self):

        if self.checkempty() is not True:

            aux = self.first
            
            while True:
                
                print(""+str(aux.get_value())+"\t(Index: "+str(aux.get_index())+ ")")

                if aux == self.last:

                    break
                else:
                    aux = aux.nextn     

    def at(self,index):

        if index >= 0 and index < self.length:

            if self.checkempty() is not True:

                aux = self.first

                while True:

                    if aux.get_index() == index:

                        return aux.get_value()

                    if aux == self.last:
                        break
                    else:
                        aux = aux.nextn 

    def atnode(self,index):

        if index >= 0 and index < self.length:

            if self.checkempty() is not True:

                aux = self.first

                while True:

                    if aux.get_index() == index:

                        return aux

                    if aux == self.last:
                        break
                    aux = aux.nextn                                      

    def isnumeric(self): #returns true if the list only have numbers (int/float type)

        if self.checkempty():

            return False

        aux = self.first

        while True:

            if type(aux.get_value()) is not int and type(aux.get_value()) is not float:

                return False

            if aux == self.last:

                break

            aux = aux.nextn    

        return True

    def sort(self): #using selection sort algorithm

        if self.checkempty() is not True:

            if self.first != self.last and self.isnumeric():

                for i in range(self.length):

                    minorpos = self.atnode(i)

                    for j in range(i+1,self.length):

                        if self.at(j) <= minorpos.get_value():

                            minorpos = self.atnode(j)

                    self.swapnodevalues(self.atnode(i),minorpos)

    def swapnodevalues(self,nodeA,nodeB):

        aux = nodeA.get_value()

        nodeA.set_value(nodeB.get_value())
        nodeB.set_value(aux) 

    def merge(self,linkedlist):

        if linkedlist.checkempty() is not True:

            if self.checkempty() is not True:

                self.last.nextn = linkedlist.first
                self.last = linkedlist.last

            else:

                self.first = linkedlist.first
                self.last = linkedlist.last

            self.updatelength()    
            self.updateindex()

            if self.isnumeric():

                self.sort()

    def reverse(self):

        if self.checkempty() is not True:

            self.first = self.last

            aux = self.first

            while True:

                if aux != self.first:

                    aux.nextn = aux.backn
                    aux.backn = aux.nextn

                elif aux == self.first:

                    aux.nextn = aux.backn
                    aux.backn = None

                if aux.nextn == None:

                    self.last = aux
                    break

                aux = aux.nextn    

            self.updateindex()

    def getlist(self, _from, _to = None):

        if self.checkempty():

            return self
            
        else:

            newlist = List()

            if _to is not None:

                for i in range(self.length):

                    if i >= _from:

                        newlist.pushback(self.at(i))

                    if i == _to:
                        break        
            else:

                for i in range(self.length):

                    if i >= _from:

                        newlist.pushback(self.at(i))

            return newlist









                                                    










