'''
Experiment No. 1 : 
In a second year computer engineering class, group A students play cricket, group B students play
badminton and group C students play football.(NOTE : While realising the group, duplicate entries should be avoided. 
Do not use SET built-in functions)
'''

'''a) List of students who play both cricket and badminton'''
def cb() :
    cb = []
    for el in cricket :
        if el in badminton :              
            cb.append(el)
    return cb
    
'''b) List of students who play either cricket or badminton but not both'''
def cbncb() :
    c = set(cricket)
    b = set(badminton)
    result = list((c - b) | (b - c))
    return result

"""c) Number of students who play neither cricket nor badminton"""
def ncnb() :
    allStudents = set()
    for el in cricket :
        allStudents.add(el)
    for el in badminton :
        allStudents.add(el)
    for el in football :
        allStudents.add(el)

    c_b_total = set(cb())
    ncnb = list(allStudents - c_b_total - set(cricket) - set(badminton))

    return ncnb

'''d) Number of students who play cricket and football but not badminton.'''
def cfnb() :
    cfnb = []
    for el in cricket :
        if el in football and cricket not in badminton :
            cfnb.append(el)
    return cfnb

cricket = ['a1','b9','a7','c4','a3']
badminton = ['b1','a1','b3']
football = ['c4','a8','c5','b3']

print("1) List of students who play both cricket and badminton :",cb())
print("2) List of students who play either cricket or badminton but not both :",cbncb())
print("3) Number of students who play neither cricket nor badminton :",ncnb())
print("4) Number of students who play cricket and football but not badminton :",cfnb())

#<-----------------END :)------------------->
