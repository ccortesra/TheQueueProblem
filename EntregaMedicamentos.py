def Parent(i):
    return int((i-1)/2)

def LeftChild(i):
    return 2*i + 1

def RightChild(i):
    return 2*i+2

def SumMili(h,dur):
    mins = h[-2:]
    hours = h[:-2]
    total_mins = (int(mins) + int(dur))%60
    if total_mins == 0: total_mins='00'
    total_hours = int(hours) +  ((int(mins) + int(dur)) >= 60)
    return str(total_hours)+str(total_mins)

class Paciente:
    def __init__(self,num_id,age,hour,t):
        self.num_id = num_id
        self.age = age
        self.hour = hour
        self.t = t

class Heap:
    def __init__(self) -> None:
        self.heap_array = []
        self.size = 0

    def SiftUp(self,i):
        while i > 0 and self.heap_array[Parent(i)].age < self.heap_array[i].age:
            self.heap_array[i], self.heap_array[Parent(i)] = self.heap_array[Parent(i)], self.heap_array[i]
            i = Parent(i)

    def SiftDown(self, i):
        maxIndex = i
        l = LeftChild(i)
        if l < self.size and self.heap_array[l].age > self.heap_array[maxIndex].age:
            maxIndex = l
        r = RightChild(i)
        if r < self.size and self.heap_array[r].age > self.heap_array[maxIndex].age:
            maxIndex = r
        
        if i != maxIndex:
            self.heap_array[i], self.heap_array[maxIndex] = self.heap_array[maxIndex], self.heap_array[i]
            self.SiftDown(maxIndex)

    def Insert(self,p):
        self.size += 1
        self.heap_array.append(p) 
        self.SiftUp(self.size-1)

    def ExtractMax(self):
        result = self.heap_array[0]
        self.heap_array[0] = self.heap_array[self.size-1]
        self.heap_array = self.heap_array[:self.size-1]
        self.size -= 1
        self.SiftDown(0)
        return result

        


def main():
    PriorityQueue = Heap()
    time = '800'
    lastTime = '800'
    while True:
        while time <= lastTime:
            entrada = input()
            if entrada == 'FIN': break
            num_id, age, hour, t  = tuple(map(int,entrada.split()))
            paciente = Paciente(num_id,age,hour,t)
            time = SumMili(str(hour),paciente.t) 
            PriorityQueue.Insert(paciente)
        
        while PriorityQueue.heap_array != []:
            nextPacient = PriorityQueue.ExtractMax()
            print(nextPacient.num_id)

        lastTime = time
        
main()
        
        
        
        
    
    
                
            


         


