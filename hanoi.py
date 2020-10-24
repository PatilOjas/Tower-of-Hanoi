import time

class Stack:

    def __init__(self,nam):
        self.topi=-1
        self.name=nam
        self.stack=[]

    def push(self, ring):
        self.stack.append(ring)

    def pop(self):
        return self.stack.pop()

    def isempty(self):
        if len(self.stack)>0:
            return False
        else:
            return True
    
    def top(self):
        return self.stack[self.topi]

    def size(self):
        return len(self.stack)

class Ring:
    def __init__(self,num):
        self.number=num


class Hanoi:
    def __init__(self,num_ring):
        self.tower_1=Stack("Tower 1")
        self.tower_2=Stack("Tower 2")
        self.tower_3=Stack("Tower 3")
        self.rings=num_ring
        for i in range(self.rings,0,-1):
            ring=Ring(i)
            self.tower_1.push(ring)
    
    def option(self):
        options={self.tower_1.name:[],self.tower_2.name:[],self.tower_3.name:[]}
        #Tower 1
        if not self.tower_1.isempty() and (self.tower_2.isempty() or (not self.tower_2.isempty() and self.tower_2.top().number>self.tower_1.top().number)):
            options[self.tower_1.name].append(self.tower_2.name)
        if not self.tower_1.isempty() and (self.tower_3.isempty() or (not self.tower_3.isempty() and self.tower_3.top().number>self.tower_1.top().number)):
            options[self.tower_1.name].append(self.tower_3.name)
        #Tower 2
        if not self.tower_2.isempty() and (self.tower_1.isempty() or (not self.tower_1.isempty() and self.tower_1.top().number>self.tower_2.top().number)):
            options[self.tower_2.name].append(self.tower_1.name)
        if not self.tower_2.isempty() and (self.tower_3.isempty() or (not self.tower_3.isempty() and self.tower_3.top().number>self.tower_2.top().number)):
            options[self.tower_2.name].append(self.tower_3.name)
        #Tower 3
        if not self.tower_3.isempty() and (self.tower_2.isempty() or (not self.tower_2.isempty() and self.tower_2.top().number>self.tower_3.top().number)):
            options[self.tower_3.name].append(self.tower_2.name)
        if not self.tower_3.isempty() and (self.tower_1.isempty() or (not self.tower_1.isempty() and self.tower_1.top().number>self.tower_3.top().number)):
            options[self.tower_3.name].append(self.tower_1.name)

        inc=[]
        for tower,opt in options.items():
            if len(opt)==0:
                inc.append(tower)
        for i in inc:
            del options[i]
        
        return options

    def move(self,src,dest):
        source=Stack("Source")
        destination=Stack("Destination")
        if src==1:
            source=self.tower_1
        if src==2:
            source=self.tower_2
        if src==3:
            source=self.tower_3
        if dest==1:
            destination=self.tower_1
        if dest==2:
            destination=self.tower_2
        if dest==3:
            destination=self.tower_3
        valid=self.option()
        if source.name in valid.keys() and destination.name in valid[source.name]:
            ring=source.pop()
            destination.push(ring)
            #print()
            #print(self.tower_1.name,self.tower_1.stack,self.tower_2.name,self.tower_2.stack,self.tower_3.name,self.tower_3.stack)
            return source.name,destination.name,destination.size(),ring.number


    def won(self):
        if self.tower_3.size()!=self.rings:
            return False
        else:
            return True

    def reset(self):
        for i in range(self.tower_3.size()):
            rn=self.tower_3.pop()
            del rn
        for i in range(self.tower_2.size()):
            rn=self.tower_2.pop()
            del rn
        for i in range(self.tower_1.size()):
            rn=self.tower_1.pop()
            del rn
        for i in range(self.rings,0,-1):
            ring=Ring(i)
            self.tower_1.push(ring)
        

    def soln(self,rings, tower_1, tower_2, tower_3) :		# 1 is main tower, 2 is auxillary tower, 3 is final tower
        if rings == 1 :
            print("Move disk 1 from" , tower_1.name, "to", tower_3.name)
            a,b,c,d=self.move(int(tower_1.name[-1]),int(tower_3.name[-1]))
            #print()
            #print(tower_1.name,tower_1.stack,tower_2.name,tower_2.stack,tower_3.name,tower_3.stack)
        else :
            time.sleep(1)
            self.soln(rings - 1, tower_1, tower_3, tower_2)
            a,b,c,d=self.move(int(tower_1.name[-1]),int(tower_3.name[-1]))
            print("Move disk", rings, " from" , tower_1.name, "to", tower_3.name)
            #print(tower_1.name,tower_1.stack,tower_2.name,tower_2.stack,tower_3.name,tower_3.stack)
            #print()
            time.sleep(1)
            self.soln(rings - 1, tower_2, tower_1, tower_3)
            

game=Hanoi(3)
# #print(game.tower_1.name,game.tower_1.stack,game.tower_2.name,game.tower_2.stack,game.tower_3.name,game.tower_3.stack)
game.soln(game.rings, game.tower_1, game.tower_2, game.tower_3)
# game.reset()
# while(not game.won()):
#     print(game.option())
#     a,b=[int(a) for a in input().split()]
#     if a==0:
#         game.reset()
#         print()
#         print(game.tower_1.name,game.tower_1.stack,game.tower_2.name,game.tower_2.stack,game.tower_3.name,game.tower_3.stack)
#     else:
#         try:
#             s,d,ds,r=game.move(a,b)
#         except:
#             print("Invalid Move")