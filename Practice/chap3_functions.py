# variable scope
def spam():
    eggs = 'spam local'
    print(eggs)


def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)


# exception handling
def div(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(div(2))
print(div(0))
