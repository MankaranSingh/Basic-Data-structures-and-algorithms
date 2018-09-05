class stack:

    def __init__(self):
        self.lst=list()

    def push(self,element):
        self.lst.append(element)

    def POP(self):
        if len(self.lst)!=0:
            return self.lst.pop()
        else:
            print('Stack underflow')

    def top(self):
        if len(self.lst)!=0:
            return self.lst[-1]
        else:
            print('Stack Empty')

    def stack_length(self):
        return len(self.lst)

    def __str__(self):
        return str(self.lst[0])
        
            
            
        
    
