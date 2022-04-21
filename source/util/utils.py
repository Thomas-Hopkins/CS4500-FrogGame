def func_bundle(funcs: tuple = None):
    """
    A bundle of functions to be executed upon calling.
    Pass functions as a tuple.
    Most effectively used with a functools.partial
    """
    for func in funcs:
        func()
