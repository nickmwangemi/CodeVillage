"""
create function 
that returns dict
call function that prints one of the values
"""


def returnDict():
    swahili = dict()

    swahili['phone'] = 'simu'
    swahili['bye'] = 'kwaheri'
    return swahili


swahili = returnDict()

print(swahili['phone'])
