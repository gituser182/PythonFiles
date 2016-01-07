__author__ = 'user0'
import os

"""
Daniel - 2015/10/16

'Cijfers'-gedeelte = 946680 mogelijke vgl maken en uitrekenen en vgl met target
In het spel Cijfers is het targetgetal tussen 101 en 999
number_list = [2,3,5,7,11,13]
vb target = 6
   oplossen : 2 * 3  = 6
              13 - 7 = 6
              3 + 2  = 5  (closest)

 vb target = 48
    oplossen: 5*7 + 13 = 48

    target = 47
    oplossen: 5 * 7 = 35
              35 + 11 = 46 (closest)

 bewerkingen lopen van links naar rechts ( + , *)
 verbeteringen: maak gebruik van sets om "dubbels" uit te sluiten
                vb 5 * 7 + 13 = 48
                   7 * 5 + 13 = 48
                   13 + 11  * 2 = 48
                   11 + 13  * 2 = 48

 Samengesteld zoeken wordt niet uitgevoerd (voorbeeld:)
 [100, 2, 75, 3, 1, 10] zoek 888
 10 + 3 = 13
 75 + 1 = 76
 76 * 13 = 988   (hier wordt een samengestelde bewerking gebruikt)
 988 - 100 = 888

 resultaat script = 100, '+', 10, '*', 2, '+', 75, '+', 1, '*', 3, '=', 888
 100 + 10 = 110
 110 * 2 = 220
 220 + 75 = 295
 295 + 1 = 296
 296 * 3 = 888


"""
#global
DEBUG = False

#declare global variables
#number_list = [2,3,5,7,11,13]  #fixed list of numbers while testing
#number_list = [7, 1, 75, 100, 9, 10]
number_list = [100, 2, 75, 3, 1, 10]
target_number = 888              #number to be calculated using elements from numberlist
lower_boundary = 101
upper_boundery = 999


### general functions
def add(num1, num2):
    """
    Addition
    """
    return num1 + num2

def sub(num1, num2):
    """
    Subtraction
    """
    return num1 - num2

def mul(num1, num2):
    """
    Multiplication
    """
    return num1 * num2

def div(num1, num2):
    """
    Division: only return fully dividable numbers
    """
    if (num1 % num2)==0:
        return num1 / num2
    else:
        return 0



def number_in_boundery(a_number, lower_bound, upper_bound):
    if a_number >= lower_bound and a_number <= upper_bound:
        return True
    else:
        return False


#dictionary will act as
ops = {'+': add,
       '-': sub,
       '*': mul,
       '/': div}
### end general functions


def generate_permutations_for_2_elements(a_list):
    """
    return all n!/(n-2)!  permutations for a list of n elements as tuples in a list
    30 permutations
    """
    returnlist = []
    for i in range(len(a_list)):
        for j in range (len(a_list)):
            if i != j: #discard 2 times same item
                returnlist.append((a_list[i],a_list[j]))
    return returnlist

def make_equations_for_2_elements(ops, a_list):
    """
    create all possible eqns(total 120) which return a value within the given boundaries
    """
    return_list = []
    for eqn in a_list:
        for operation in ops.keys():
            val = ops[operation](eqn[0], eqn[1]) #use dictionary
            if number_in_boundery(val,lower_boundary,upper_boundery):
                return_list.append((eqn[0], operation, eqn[1], '=', val)) #tuple
    return return_list



def generate_permutations_for_3_elements(a_list):
    """
    return all n!/(n-3)! permutations for a list of n elements as tuples in a list
    120 permutations
    """
    returnlist = []
    for i in range(len(a_list)):
        for j in range (len(a_list)):
            for k in range(len(a_list)):
                if i != j and i != k and j != k: #discard 3 times same item
                    #print a_list[i], a_list[j]
                    returnlist.append((a_list[i],a_list[j], a_list[k]))
    return returnlist


def make_equations_for_3_elements(ops, a_list):
    """
    create all possible eqns (total 1920 = 120 permutations * 4 * 4 ops)
    which return a value within the given boundaries
    """
    return_list = []
    for eqn in a_list:

        for first_operation in ops.keys():
            val = ops[first_operation](eqn[0], eqn[1]) #use dictionary
            for second_operation in ops.keys():
                val2 = ops[second_operation](val, eqn[2])

                if number_in_boundery(val2,lower_boundary,upper_boundery):
                    return_list.append( (eqn[0], first_operation, eqn[1], second_operation, eqn[2],'=', val2) ) #tuple
    return return_list

def generate_permutations_for_4_elements(a_list):
    """
    return all n!/(n-4)! permutations for a list of n elements as tuples in a list
    360 permutations
    """
    returnlist = []
    for i in range(len(a_list)):
        for j in range (len(a_list)):
            for k in range(len(a_list)):
                for l in range(len(a_list)):
                    if i != j and i != k and i != l and j != k and j != l and k != l: #discard 4 times same item
                        returnlist.append((a_list[i],a_list[j], a_list[k], a_list[l]))
    return returnlist

def make_equations_for_4_elements(ops, a_list):
    """
    create all possible eqns  which return a value within the given boundaries
    total = 23040    360 permutations * 4 * 4 * 4 operations
    """
    return_list = []
    for eqn in a_list:

        for first_operation in ops.keys():
            val = ops[first_operation](eqn[0], eqn[1]) #use dictionary
            for second_operation in ops.keys():
                val2 = ops[second_operation](val, eqn[2])
                for third_operation in ops.keys():
                    val3 = ops[third_operation](val2, eqn[3])

                    if number_in_boundery(val2,lower_boundary,upper_boundery):
                        return_list.append( (eqn[0], first_operation, eqn[1], second_operation, eqn[2],\
                                     third_operation, eqn[3],'=', val3) ) #tuple
    return return_list


def generate_permutations_for_5_elements(a_list):
    """
    return all n!/(n-5)! permutations for a list of n elements as tuples in a list
    720 permutations
    """
    returnlist = []
    for i in range(len(a_list)):
        for j in range (len(a_list)):
            for k in range(len(a_list)):
                for l in range(len(a_list)):
                    for m in range(len(a_list)):
                        #discard 5 same element choices
                        if i != j and i != k and i != l and i != m and j != k and j != l and j != m \
                                and k != l and k !=m and l != m:
                            returnlist.append((a_list[i],a_list[j], a_list[k], a_list[l], a_list[m]))
    return returnlist

def make_equations_for_5_elements(ops, a_list):
    """
    create all possible eqns  which return a value within the given boundaries
    total = 184320    720 permutations * 4 * 4 * 4 *4 operations
    """
    return_list = []
    for eqn in a_list:

        for first_operation in ops.keys():
            val = ops[first_operation](eqn[0], eqn[1]) #use dictionary
            for second_operation in ops.keys():
                val2 = ops[second_operation](val, eqn[2])
                for third_operation in ops.keys():
                    val3 = ops[third_operation](val2, eqn[3])
                    for fourth_operation in ops.keys():
                        val4 = ops[fourth_operation] (val3, eqn[4])

                        if number_in_boundery(val2,lower_boundary,upper_boundery):
                            return_list.append( (eqn[0], first_operation, eqn[1], second_operation, eqn[2],\
                                     third_operation, eqn[3], fourth_operation, eqn[4], '=', val4) ) #tuple
    return return_list


def generate_permutations_for_6_elements(a_list):
    """
    return all n!/(n-6)! permutations for a list of n elements as tuples in a list
    720 permutations
    """
    returnlist = []
    for i in range(len(a_list)):
        for j in range (len(a_list)):
            for k in range(len(a_list)):
                for l in range(len(a_list)):
                    for m in range(len(a_list)):
                        for n in range(len(a_list)):
                        #discard 5 same element choices
                            if i != j and i != k and i != l and i != m and i != n\
                                and j != k and j != l and j != m and j != n\
                                and k != l and k !=m and k != n\
                                and l != m and l != n and m != n:
                                returnlist.append((a_list[i],a_list[j], a_list[k], a_list[l], a_list[m], a_list[n]))
    #print "len list6 = ", len(returnlist)
    return returnlist

def make_equations_for_6_elements(ops, a_list):
    """
    create all possible eqns  which return a value within the given boundaries
    total = 737280    720 permutations * 4 * 4 * 4 *4 *4 operations
    """
    return_list = []
    for eqn in a_list:

        for first_operation in ops.keys():
            val = ops[first_operation](eqn[0], eqn[1]) #use dictionary
            for second_operation in ops.keys():
                val2 = ops[second_operation](val, eqn[2])
                for third_operation in ops.keys():
                    val3 = ops[third_operation](val2, eqn[3])
                    for fourth_operation in ops.keys():
                        val4 = ops[fourth_operation] (val3, eqn[4])
                        for fifth_operation in ops.keys():
                            val5 = ops[fifth_operation] (val4, eqn[5])

                            if number_in_boundery(val2,lower_boundary,upper_boundery):
                                return_list.append( (eqn[0], first_operation, eqn[1], second_operation, eqn[2],\
                                     third_operation, eqn[3], fourth_operation, eqn[4], \
                                                 fifth_operation, eqn[5],'=', val5) ) #tuple
    return return_list

def Perform_Check_2():
    #generate all permutations for 2 elements from list
    list_per2 = []
    list_per2 = generate_permutations_for_2_elements(number_list)
    Eq_list2 = make_equations_for_2_elements(ops, list_per2)

    #check if exact match is found
    for eqn in Eq_list2:
        if eqn[-1] == target_number:
            print "MATCH FOUND ", eqn

    #check for closest match
    closest_list = []
    closest = [float('inf')]
    for eqn in Eq_list2:
        if abs(target_number - eqn[-1]) <= abs(target_number - closest[-1]):
            closest = eqn
            if eqn[-1] != target_number:
                closest_list.append(eqn)
    print "Closest match is ", closest


def Perform_Check_3():
    #generate all permutations for 3 elements from list
    list_per3 = []
    list_per3 = generate_permutations_for_3_elements(number_list)
    Eq_list3 =  make_equations_for_3_elements(ops, list_per3)

    #check if exact match is found
    for eqn in Eq_list3:
        if eqn[-1] == target_number:
            print "MATCH FOUND ", eqn

    #check for closest match
    closest_list = []
    closest = [float('inf')]
    for eqn in Eq_list3:
        if abs(target_number - eqn[-1]) <= abs(target_number - closest[-1]):
            closest = eqn
            if eqn[-1] != target_number:
                closest_list.append(eqn)
    print "Closest match is ", closest


def Perform_Check_4():
    #generate all permutations for 4 elements from list
    list_per4 = []
    list_per4 = generate_permutations_for_4_elements(number_list)
    Eq_list4 =  make_equations_for_4_elements(ops, list_per4)


    #check if exact match is found
    for eqn in Eq_list4:
        if eqn[-1] == target_number:
            print "MATCH FOUND ", eqn

    #check for closest match
    closest_list = []
    closest = [float('inf')]
    for eqn in Eq_list4:
        if abs(target_number - eqn[-1]) <= abs(target_number - closest[-1]):
            closest = eqn
            if eqn[-1] != target_number:
                closest_list.append(eqn)
    print "Closest match is ", closest


def Perform_Check_5():
    #generate all permutations for 5 elements from list
    list_per5 = []
    list_per5 = generate_permutations_for_5_elements(number_list)
    Eq_list5 =  make_equations_for_5_elements(ops, list_per5)

    #check if exact match is found
    for eqn in Eq_list5:
        if eqn[-1] == target_number:
            print "MATCH FOUND ", eqn

    #check for closest match
    closest_list = []
    closest = [float('inf')]
    for eqn in Eq_list5:
        if abs(target_number - eqn[-1]) <= abs(target_number - closest[-1]):
            closest = eqn
            if eqn[-1] != target_number:
                closest_list.append(eqn)
    print "Closest match is ", closest

def Perform_Check_6():
    #generate all permutations for 6 elements from list
    list_per6 = []
    list_per6 = generate_permutations_for_6_elements(number_list)
    Eq_list6 =  make_equations_for_6_elements(ops, list_per6)


    #check if exact match is found
    for eqn in Eq_list6:
        if eqn[-1] == target_number:
            print "MATCH FOUND ", eqn

    #check for closest match
    closest_list = []
    closest = [float('inf')]
    for eqn in Eq_list6:
        if abs(target_number - eqn[-1]) <= abs(target_number - closest[-1]):
            closest = eqn
            if eqn[-1] != target_number:
                closest_list.append(eqn)
    print "Closest match is ", closest

def play():
    print "Le compte est bon?\n"
    print "Given numbers are ", number_list
    print "Target_number is ", target_number
    print

    if target_number in number_list:
        print "number found in list"
        exit()

    print "\nUsing 2 elements"
    Perform_Check_2()

    print "\nUsing 3 elements"
    Perform_Check_3()

    print "\nUsing 4 elements"
    Perform_Check_4()

    print "\nUsing 5 elements"
    Perform_Check_5()

    print "\nUsing 6 elements"
    Perform_Check_6()


def boundary_test():
    """
    testing boundaries for numbers. Working!
    """
    for i in range(90,1010):
        if not number_in_boundery(i,lower_boundary,upper_boundery):
            print "number ", i, " is not in boundery"


def main():
    """
    Main part of the application - 16/10/2015
    """
    #boundary_test()
    play()



"""
Start the main body of the program, protected by 'try - except'
"""
if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print "Error"
        print str(e)
        os._exit(1)
