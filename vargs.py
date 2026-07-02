# *args indicates that this function can take a variable number of parents (positional)
# **kwargs indicates the same but for named arguments
def v_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Named arguments: ", kwargs)


v_args(1, 4, 5, named="named1", test="test2")
