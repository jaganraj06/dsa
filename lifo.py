def create_stack():
    return []
def is_empty(stack):
    return len(stack)==0
def push_stack(stack,value):
    stack.append(value)
    print("insert item:"+str(value))
def pop_stack(stack):
    if(is_empty(stack)):
        print("is emppty")
    else:
        print("top value")
        stack.pop()
def show(stack):
    print("element in the stack")
    for item in stack:
        print(item)


s1=create_stack()
push_stack(s1,3)
push_stack(s1,4)
push_stack(s1,5)
pop_stack(s1)
show(s1)

        
    

    
    