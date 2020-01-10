# CSci 1133 HW 7
# Nicholas Mayer
# HW Problem A
#
# This script will create a MnEmployee class object

class MnEmployee:
    def __init__(self,ID=0,salary=0,otWages=0,addWages=0,totalWages=0):
        self.employeeID = ID
        self.__salary = float(salary)
        self.__otWages = float(otWages)
        self.__addWages = float(addWages)
        self.__totalWages = float(totalWages)
    def __lt__(self, other):
        if self.__totalWages < other.__totalWages:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.__totalWages > other.__totalWages:
            return True
        else:
            return False
    def __repr__(self):
        return (str(self.employeeID)+','+str(self.__salary)+','
                +str(self.__otWages)+','+str(self.__addWages)+','
                +str(self.__totalWages)+'\n')
    def __str__(self):
        return ('%12s\t%12s\t%12s\t%12s\t%12s' %
                (str(self.employeeID),str(self.__salary),
               str(self.__otWages),str(self.__addWages),
               str(self.__totalWages)))
