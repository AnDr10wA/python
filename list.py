
def  simple_func(*args):
    return(type (args))	
	

test = simple_func(False, {'name':'Anon'}, true, 56 < False)
print(test)