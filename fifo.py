print("test")
a=[1,2,3,4,5,6,7]
arr_length = 8
def enque(b):
    if isfull():
      print("isfull")
    else:
       a.append(b)
def deque():
   del a[0]
def empty():
   a.clear()
def isEmpty():
   return len(a) <= 0
def isfull():
   return len(a) >= arr_length
def peek():
   if(isEmpty()):
      return "List is empty"
   else:
      return a[0]
print(a)
enque(8)
enque(9)
print("enque--",a)
deque()
print("deque--",a)
c = peek()
print("peek---",c)
empty()
print("empty--",a)
d = peek()
print(d)
