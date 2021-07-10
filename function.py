"""functions"""


def first_function(args):
    """first_function"""
    print('\n ==first_function("hamid")==', args)


first_function('hamid')


def second_function(*args):
    """second_function"""
    print('\n ==second_function("Hamid",1,"Eman")==', args)


second_function('Hamid', 1, 'Eman')


def third_function(**args):
    """third_function"""
    print('\n ==third_function(arg1="Hamid", arg2=1, arg3="Eman")==', args)


third_function(arg1='Hamid', arg2=1, arg3='Eman')
