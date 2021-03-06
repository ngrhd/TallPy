from xml.etree import ElementTree as ET
import sys


##Validation if no intergers are inputed

'''def A():
    while True:
        A.x = input('Enter party name: ')
        if A.x.isdigit() == True:
            print('Please enter a name.')
            continue
        else:
            return A.x
            break
'''


def A(party_name):
    A.x = party_name
    return A.x


'''def initialize_x(value)
    x = value
'''
#Initialization of ElementTree and Finding the list/numbers of each Tag
def B():
    tree = ET.parse('Bills.xml')
    root = tree.getroot()
    B.billfixed = tree.findall('BILLFIXED')
    B.billcl = tree.findall('BILLCL')
    B.billdue = tree.findall('BILLDUE')
    B.billoverdue = tree.findall('BILLOVERDUE')

def C():
    y= A.x
    b = []
    #Itering and zipping the orphaned children
    for fixed, cl, due, overdue in zip(B.billfixed, B.billcl, B.billdue, B.billoverdue):
        #Getting it all lower case and then comparing
        if y.lower() == fixed.find('BILLPARTY').text.lower():

            date = fixed.find('BILLDATE').text
            ref= fixed.find('BILLREF').text
            party = fixed.find('BILLPARTY').text

           b = ' * [Inv # {}] [Date {}] [Amt {}] [Due date {}] [Overdue by {} days]'.format(
            ref, date, cl.text, due.text, overdue.text
    )
            print('******************************************************************')
        else:
            print('Party name not found!')
            sys.exit()


def main_loop(for_a):
    A(for_a)
    B()
    C()
    from_c =
    return


if __name__ == '__main__':
    main_loop()