import numpy as np
import sys
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

BODMAS  = ["^","/","*","+","-"]
trig_func = ["sin","arcsin","cos","arccos","tan","arctan"]
eq_dec = ""
tries = 0
math_constants = {
    "pi": np.pi, #pi
    "e": np.e, #euler's number
    "c": 299792458.0, #speed of light
    "h": 6.62607015e-34, #planck's constant
    "G": 6.6743e-11, #universal gravitational constant
    "Qe": 1.602176634e-19, #charge on an electron
    "N": 6.02214076e+23, #avogadro's number
    "kb": 1.380649e-23, #boltzmann constant
    "Ryd": 10973731.568508, #rydberg constant
    "Mp": 1.67262192369e-27, #mass of proton
    "Mn": 1.67492749804e-27, #mass of neutron
    "Me": 9.1093837015e-31, #mass of electron
    "R": 8.314472, #gas constant
    "F": 96485.3321 #faraday's constant
}

def absolute(num):
    num = float(num)
    if num < 0.0:
        num *= -1
    return num

def index_var(temp, search):
    loc = 0
    while loc < length(temp):
        if temp[loc] == search:
            return loc
        loc += 1

def split(instring):
    eq_split = []
    temp = ''
    for i in range(length(instring)):
        if instring[i] != " ":
            temp += instring[i]
        else:
            eq_split = append(eq_split, temp)
            temp = ''
    eq_split = append(eq_split, temp)
    final_eq = []
    for j in eq_split:
        if j != '':
            final_eq = append(final_eq, j)
    return final_eq

def insert(instring, index, insert):
    temp = []
    for i in range(length(instring)):
        if i == index:
            temp = append(temp, insert)
        temp = append(temp, instring[i])
    if index == length(instring) or length(instring) == 0:
        temp = append(temp, insert)
    return temp

def length(instring):
    count = 0
    try:
        while instring[count] != "":
            count += 1
    except:
        pass
    return count

def append(list, element):
    temp = list
    list = ["" for i in range(len(temp) + 1)]
    for i in range(len(temp)):
        list[i] = temp[i]
    list[len(list) - 1] = element
    return list
    
def boom(instring, index):
    temp = []
    counter = 0
    while counter < length(instring):
        if counter != index:
            temp = append(temp, instring[counter])
        counter += 1
    return temp

def solve(num1,num2,oper):
    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1 * num2
    elif oper == "/":
        if num2 == 0:
            return np.inf
        return num1 / num2
    else:
        if float(num1) == 0.0 and float(num2) < 0:
            return np.inf
        return num1**num2

def operator_selection(temp):
    for oper in BODMAS:
        for i in range(length(temp)):
            if oper == temp[i]:
                return i, oper
def selection_numbers(temp, index):
    num1 = 0
    num2 = 0
    dec, inn = index - 1, index + 1
    num1, num2 = float(temp[dec]), float(temp[inn])
    return num1, num2, dec, inn
        
def reorder(temp):
    index, op = operator_selection(temp)
    num1, num2, dec, inn = selection_numbers(temp, index)
    ans = solve(num1, num2, op)
    for i in range(dec, inn + 1):
        temp = boom(temp, dec)
    temp = insert(temp, dec, str(ans))
    return temp

def brac_seperate(temp):
    brac_eq = " "
    brac_found = False
    if "(" in temp:
        brac_found = True
        index_open = index_var(temp, "(")
        index_close = index_open
        close_found = False
        while not close_found:
            if temp[index_close] == "(":
                index_open = index_close
            if temp[index_close] == ")":
                close_found = True 
            index_close += 1
        for index in range(index_open + 1, index_close - 1):
            brac_eq += str(temp[index])
            brac_eq += " "
        return brac_eq, brac_found, index_open
    else:
        return temp, brac_found, -1

def eq_seperate(eq, eq_dec):
    if eq[0].lower() == "x":
        eq_dec += " " + eq[0] + " "
    elif (eq[0] >= "0" and eq[0] <= "9") or (eq[0].lower() >= "a" and eq[0].lower() <= "z") or eq[0] == "-":
        eq_dec += eq[0]
    else:
        eq_dec += eq[0] + " "
    for i in range(1,len(eq)):
        if (eq[i] == "(" or eq[i] == "x") and (eq[i - 1] not in BODMAS and eq[i - 1] != "(") and i != 0:
            eq_dec += " * "
        if eq[i].lower() == "x":
            eq_dec += " " + eq[i] + " "
        elif eq[i] == "C" or eq[i] == "P":
            eq_dec += " " + eq[i] + " "
        elif (eq[i] >= "0" and eq[i] <= "9") or (eq[i].lower() >= "a" and eq[i].lower() <= "z" and eq[i] != "x") or eq[i] == ".":
            eq_dec += eq[i]
        elif eq[i] == "-" and (eq[i - 1] in BODMAS or eq[i - 1] == "(" or eq[i - 1] == "|"):
            eq_dec += eq[i]
        else:
            eq_dec += " " + eq[i] + " "
    return split(eq_dec)

def minus_minus_plus(temp):
    for i in range(length(temp)):
        try:
            if float(temp[i]) < 0 and temp[i - 1] == "-":
                temp[i - 1] = "+"
                temp[i] = str(float(temp[i]) * -1)
        except:
            pass
    return temp

def trignometry(instring, tries, index):
    global mode
    if tries == 1:
        mode = input("MODE: deg  rad: ")
        while mode != "deg" and mode != "rad":
            mode = input("ENTER VALID MODE: deg  rad: ")
    func = instring[index]
    temp = []
    index += 1
    while instring[index - 1] != ")" and index < len(instring):
        temp = append(temp, instring[index])
        index += 1
    end_brac = index
    num = float(temp[index_var(temp, "(") + 1])
    if mode == "deg" and func != "arcsin" and func != "arccos" and func != "arctan":
        num = np.deg2rad(num)
    if func == "sin":
        return str(round(np.sin(num), 11)), end_brac
    elif func == "cos":
        return str(round(np.cos(num), 11)), end_brac
    elif func == "tan":
        if (num/np.pi) % 1 == 0.5:
            return np.inf, end_brac
        ans = str(round(np.tan(num), 11))
        if float(ans) > 1.0e5 or float(ans) < -1.0e5:
            ans = np.inf
        return ans, end_brac
    elif func == "arcsin":
        ans =  str(np.arcsin(num))
        if mode == "deg":
            return str(float(ans) * (180/np.pi)), end_brac
        return ans, end_brac
    elif func == "arccos":
        ans =  str(np.arccos(num))
        if mode == "deg":
            return str(float(ans) * (180/np.pi)), end_brac
        return ans, end_brac
    else:
        ans =  str(np.arctan(num))
        if mode == "deg":
            return str(float(ans) * (180/np.pi)), end_brac
        return ans, end_brac
    
def factorial(temp, index):
    if temp[index - 1] == "0":
        return "1"
    else:
        try:
            fact = int(temp[index - 1])
        except:
            print ("MATH ERROR!!!")
            sys.exit()
        instring = fact
        for i in range(fact - 1, 0, -1):
            instring *= i
        return str(instring)

def logarithm(instring, index):
    func = instring[index]
    temp = []
    index += 1
    while instring[index - 1] != ")" and index < len(instring):
        temp = append(temp, instring[index])
        index += 1
    end_brac = index
    num = float(temp[index_var(temp, "(") + 1])
    if func == "log":
        return str(np.log10(num)), end_brac
    elif func == "ln":
        return str(np.log(num)), end_brac
    
def Combination(string, index):
    n = int(string[index - 1])
    r = int(string[index + 1])
    den = math_main(eq_seperate(str(r)+"!"+"*"+str(n - r)+"!", ""))
    rep = "(",str(n),"!","/",den,")"
    for i in range(3):
        string = boom(string, index - 1)
    for j in range(length(rep)):
        string = insert(string, index - 1 + j, rep[j])
    return string

def Permutation(string, index):
    n = int(string[index - 1])
    r = int(string[index + 1])
    rep = "(",str(n),"!","/",str(n - r),"!",")"
    for i in range(3):
        string = boom(string, index - 1)
    for j in range(length(rep)):
        string = insert(string, index - 1 + j, rep[j])
    return string

def func(instring):
    count = 0
    global tries
    while count < length(instring):
        if (instring[count] == "ln" or instring[count] == "log") or (instring[count] in trig_func) or instring[count] == "!":
            found = True
            if instring[count] == "!":
                instring = boom(instring, count)
                instring[count - 1] = factorial(instring, count)
                count = 0
                break
            if instring[count + 2] != "(":
                instring = insert(instring, count + 2, "(")
                instring = insert(instring, count + 4, ")")
            if instring[count] == "ln" or instring[count] == "log":
                sol, loc = logarithm(instring, count)
            else:
                tries += 1
                sol, loc = trignometry(instring, tries, count)
            for iter in range(count, loc):
                instring = boom(instring, count)
            instring = insert(instring, count, sol)
            count = 0
        else:
            found = False
            count += 1
    return instring, found

def integration(lower_limit, upper_limit):
    div = (upper_limit - lower_limit)/100000
    area = 0
    while round(lower_limit, 7) != round(upper_limit, 7):
        array = temp[:]
        for i in range(length(eq_dec)):
            if array[i] == "x":
                array[i] = lower_limit
            elif array[i] == "-x":
                array[i] = "-" + lower_limit
        height = float(math_main(array))
        area += (div * height)
        lower_limit += div
    return round(area, 10)

def differentiation(eq_dec, temp):
    value = input("Enter the value of x: ")
    x2 = float(value) + 0.000000001
    for i in range(length(eq_dec)):
        if eq_dec[i] == "x":
            eq_dec[i] = value
            temp[i] = x2
        elif eq_dec[i] == "-x":
            eq_dec[i] = "-" + value
            temp[i] = "-" + x2
    y1 = float(math_main(eq_dec))
    y2 = float(math_main(temp))
    return (y2-y1)/(0.000000001)
        
def quadratic(a, b, c):
    d = b**2 + (-4 * a * c)
    den = 2*a
    b = -1 * b
    return round((b + d*0.5)/den, 5), round((b - d*0.5)/den, 5)

def summation(lower_limit, upper_limit):
    sum = 0
    while lower_limit != upper_limit + 1:
        array = temp[:]
        for i in range(length(eq_dec)):
            if array[i] == "x":
                array[i] = lower_limit
            elif array[i] == "-x":
                array[i] = "-" + lower_limit
        num = float(math_main(array))
        sum += num
        lower_limit += 1
    return round(sum, 10)

def product_summation(lower_limit, upper_limit):
    sum = 1
    while lower_limit != upper_limit + 1:
        array = temp[:]
        for i in range(length(eq_dec)):
            if array[i] == "x":
                array[i] = lower_limit
            elif array[i] == "-x":
                array[i] = "-" + lower_limit
        num = float(math_main(array))
        sum *= num
        lower_limit += 1
    return round(sum, 10)

def graph(lower_limit, upper_limit):
    y = []
    x = []
    plt.xlim(lower_limit, upper_limit)
    if ("sin" in temp or "cos" in temp or "tan" in temp) and (upper_limit/np.pi % 1 == 0.5 or upper_limit/np.pi % 1 == 0):
        div = np.pi/50
    else:
        div = 1
    while round(lower_limit, 7) != round(upper_limit + div, 7):
        x = append(x, lower_limit)
        array = temp[:]
        for i in range(length(eq_dec)):
            if array[i] == "x":
                array[i] = lower_limit
            elif array[i] == "-x":
                array[i] = "-" + lower_limit
        num = float(math_main(array))
        y = append(y, num)
        lower_limit += div
    plt.plot(x,y)
    plt.show()

def limit(eq_dec, lim):
    lim = lim + 0.000000001
    for i in range(length(eq_dec)):
        if eq_dec[i] == "x":
            eq_dec[i] = lim
        elif eq_dec[i] == "-x":
            eq_dec[i] = "-" + lim
    return round(float(math_main(eq_dec)), 10)

def math_main(eq_dec): 
    for index, i in enumerate(eq_dec):
        if i in math_constants:
            eq_dec[index] = str(math_constants[i])
    length_eq = length(eq_dec)
    i = 0
    while i < length_eq:
        if eq_dec[i] == "C":
            eq_dec = Combination(eq_dec, i)
        if eq_dec[i] == "P":
            eq_dec = Permutation(eq_dec, i)
        length_eq = length(eq_dec)
        i += 1
    temp, brac_found, brac_open = brac_seperate(eq_dec)
    while brac_found:
        if brac_found:
            temp_eq = split(temp)
            len = length(temp_eq) + 2
        counter = 0
        iter = 0
        while counter < length(temp_eq):
            temp_eq, status = func(temp_eq)
            if temp_eq[counter] in BODMAS and not status:
                temp_eq = reorder(temp_eq)
                counter = 0
            if not status and length(temp_eq) != 1 and iter == 0:
                counter = 0
                iter = 1
            if length(temp_eq) == 1:
                break
            counter += 1
        if brac_found:
            for i in range(len):
                eq_dec = boom(eq_dec, brac_open)
            eq_dec = insert(eq_dec, brac_open, temp_eq[0])
        temp, brac_found, brac_open = brac_seperate(eq_dec)
    eq_dec = minus_minus_plus(eq_dec)
    oper = 0
    iter = 0
    while oper < length(eq_dec):
        eq_dec, status = func(eq_dec)
        if eq_dec[oper] in BODMAS and not status:
            eq_dec = reorder(eq_dec)
            oper = 0
        if not status and length(eq_dec) != 1 and iter == 0:
            oper = 0
            iter = 1
        if length(eq_dec) == 1:
            break
        oper += 1
    return eq_dec[0]

mode = int(input("1. differentiate\n2. integrate\n3. Summation\n4. Product Summation\n5. Quadratic\n6. Graph\n7. Limit\n8. Basic Maths\n: "))
if mode != 5:
    eq = input("Enter the equation: ")
    eq_dec = eq_seperate(eq, eq_dec)
    for i in range(1, len(eq_dec) - 1):
        if eq_dec[i] == "-" and eq_dec[i + 1] != "(":
            eq_dec[i] = "+"
            if eq_dec[i + 1] != "x":
                eq_dec[i + 1] = str(float(eq_dec[i + 1]) * -1)
            else:
                eq_dec[i + 1] = "-x"
    if mode == 1 or mode == 2 or mode == 3 or mode == 4 or mode == 6:
        temp = eq_seperate(eq, "")
if mode == 1:
    if "x" not in eq_dec:
        print ("0")
    else:
        print (differentiation(eq_dec, temp))
elif mode == 2:
    lower_limit = math_main(eq_seperate(input("Enter the lower limit: "), ""))
    upper_limit = math_main(eq_seperate(input("Enter the upper limit: "), ""))
    print (integration(float(lower_limit), float(upper_limit)))
elif mode == 3:
    valid = False
    while not valid:
        try:
            lower_limit = int(math_main(eq_seperate(input("Enter the lower limit: "), "")))
            upper_limit = int(math_main(eq_seperate(input("Enter the upper limit: "), "")))
            valid = True
        except:
            pass
    print (summation(lower_limit, upper_limit))
elif mode == 4:
    valid = False
    while not valid:
        try:
            lower_limit = int(math_main(eq_seperate(input("Enter the lower limit: "), "")))
            upper_limit = int(math_main(eq_seperate(input("Enter the upper limit: "), "")))
            valid = True
        except:
            pass
    print (product_summation(lower_limit, upper_limit))
elif mode == 5:
    print ("ax^2 + bx + c = 0")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    print (quadratic(a, b, c))
elif mode == 6:
    lower_limit = math_main(eq_seperate(input("Enter the lower limit: "), ""))
    upper_limit = math_main(eq_seperate(input("Enter the upper limit: "), ""))
    graph(float(lower_limit), float(upper_limit))
elif mode == 7:
    lim = int(input("Enter Limit: "))
    print (limit(eq_dec, lim))
else:
    print (math_main(eq_dec))