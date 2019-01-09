
def simple_func(*argi):
    
    if len(argi) == 0 :
        return( print('Net nicego'))
    if len(argi) == 1 :
    	return (argi)

    a = list()
    for element in argi:
        a.append(type(element)) 
        print (a)
    d = dict.fromkeys(a)
    d = dict.fromkeys(a, 2)
    print(d)

simple_func(5, 'Hello' , 4)