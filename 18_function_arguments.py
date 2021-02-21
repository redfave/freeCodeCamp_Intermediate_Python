def function_1(a, b, c, d=4):
    print(a, b, c, d)


function_1(c=1, b=2, a=3, d=4)
print('\n')


# optional named arguments
def function_2(a, b, *pos_args, **kw_args):
    print(a, b)
    for pos_arg in pos_args:  # pos_args is a tuple
        print(pos_arg)
    for key in kw_args:  # kw_args is a dictionary
        print(kw_args[key])


function_2('a', '2', 3, 4, 5, foo='bar', baz=8)
print('\n')


# forced named arguments
def function_3(a, *pos_args, y, z):
    print(a)
    for arg in pos_args:
        print(arg)
    print(y, z)


function_3(1, 2, y=3, z=4)
print('\n')

# unpacking
function_1(*(1, 2, 3))  # length of iterable must match the parameter count
print('\n')
function_1(**{'c': 1, 'b': 3, 'a': 2, 'd': 7})  # keys must match parameter names

global_number_var = 1


def global_scope_access():
    # global_number_var = 7 # creates a local variable
    global global_number_var
    print(f'Initial value {global_number_var}')
    global_number_var += 2
    print(f'Local value {global_number_var}')


global_scope_access()
print(f'Global value {global_number_var}')


#pass by object reference
def immutable_manipulation(x):
    x = 5 #local variable x as intigers are immutable
var = 10
immutable_manipulation(var)
print(var)
print('\n')

def mutable_manipulation(list):
    #list = [100,200,500] #reference rebinding causes the loss of changes after method execution
    list += [99,100] # not a reference rebinding, works
    #list = list + [99,100] # a reference rebinding, works not

    list.append('appended')
    list[0]=-20 #immutable member of mutable objects can be changed

l = [1, 'a', 'b']
mutable_manipulation(l)
print(l)


