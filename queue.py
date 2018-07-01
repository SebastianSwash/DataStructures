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

        self.nextn = next

    def get_nextn(self):

        return self.nextn


class Queue:

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

    def enqueue(self,value):

        if self.checkempty():

            self.first = self.last = Node(value)

        else:

            node = Node(value)

            self.last.nextn = node
            self.last = node

        self.length += 1    

    def dequeue(self):

        if self.checkempty() is not True:

            if self.first == self.last:

                self.first = self.last = None

            else:

                self.first = self.first.nextn

            self.length -= 1

    def isnumeric(self):

        if self.checkempty():

            return False

        else:

            aux = self.first

            while True:


                if type(aux.get_value()) is not int and type(aux.get_value()) is not float:

                    return False


                if aux == self.last:

                    return True

                aux = aux.nextn

    def sort(self):

        if self.checkempty() is not True:

            if self.isnumeric():

                if self.first != self.last:

                    aux = self.first

                    while True:

                        minpos = aux
                        aux2 = aux.nextn

                        if aux2 is None:
                            break

                        while True:

                            if aux2.get_value() <= minpos.get_value():

                                minpos = aux2

                            if aux2 == self.last:
                                break
                            aux2 = aux2.nextn

                        auxvalue = aux.get_value()
                        aux.set_value(minpos.get_value())
                        minpos.set_value(auxvalue)

                        if aux == self.last:
                            break 
                        aux = aux.nextn       

    def printqueue(self):

        if self.checkempty() is not True:

            aux = self.first

            while True:

                print(aux.get_value())

                if aux == self.last:
                    break
                aux = aux.nextn






