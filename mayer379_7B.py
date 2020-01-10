# CSci 1133 Hw 7
# Nicholas Mayer
# HW Problem B
#
# 

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

def getOrder():
    order = input('Sort in (A)scending or (D)escending order? ')
    if order in 'ADad':
        return order
    else:
        print('Invalid input, please re-enter:')
        getOrder()

def main():
    keepGoing = True
    while keepGoing:
        fName = input('Enter input file name: ')
        try: # try/except block for file errors
            fObj = open(fName, 'r')
        except FileNotFoundError:
            print('Input error: No such file or directory. Please re-enter.')
            continue
        empList = fObj.readlines()
        fObj.close()
        order = getOrder()
        finalList = []
        for line in empList[1:]:
            line = line.strip()
            line = line.split(',')
            employee = MnEmployee(line[0],line[1],line[2],line[3],line[4])
            finalList.append(employee)
        if order == 'A':
            sortedList = sorted(finalList)
        if order == 'D':
            sortedList = sorted(finalList, reverse = True)
        while True:
            numLines = input('How many employee records would you like to print? ')
            if numLines.isnumeric() == True:
                numLines = int(numLines)
                if numLines < (len(empList)):
                    if numLines > 0:
                        break
            print('Error:', numLines, 'is not a valid selection, try again.')
        print('\n%12s\t%12s\t%12s\t%12s\t%12s'
              % ('Employee ID','Wages','Overtime','Additional','Total'))
        for line in sortedList[:numLines]:
            print(line)
        print()
        save = input('Save sorted list? (Enter "Y" or "y" to save) ')
        if save in ('y','Y'):
            filename = input('Enter name of output file: ')
            wObj = open(filename, 'w', encoding = 'UTF-8')
            wObj.write('EmployeeID,Wages,Overtime,Additional,Total\n')
            for line in sortedList[:numLines]:
                wObj.write(line.__repr__())        
        tryAgain = input('Enter "Y" or "y" to continue: ')
        if tryAgain not in ['Y', 'y']:
            keepGoing = False
if __name__ == '__main__':
    main()
