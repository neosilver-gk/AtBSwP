def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def becon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
becon()
print(eggs) # prints 'global'
