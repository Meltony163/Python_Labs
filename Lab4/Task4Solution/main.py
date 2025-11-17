import json
class Queue:
  def __init__(self):
    self.items = []
  def push(self,value):
    self.items.append(value)
  def pop(self):
    if len(self.items) == 0:
      print("cannot pop from an empty queue.")
      return None
    else:
      return self.items.pop(0)
  def Isempty(self):
    if len(self.items) == 0:
      return True
    else:
      return False
  def DisplayQueue(self):
    for item in self.items:
      print(item)


class QueueOutOfRangeException(Exception):
    def __init__(self):
        super().__init__("Can't Insert In Full Queue")

class NameExist(Exception):
    def __init__(self):
        super().__init__("Queue Name Already Exists")

class NamedQueue(Queue):
    QueuesItems={}
    def __init__(self,_Name,_Size):
        if _Name in NamedQueue.QueuesItems:
            raise NameExist
        else:
            super().__init__()
            self.Name = _Name
            self.Size = _Size
            NamedQueue.QueuesItems[_Name]=self

    def push(self,value):
        if len(self.items)==self.Size:
            raise QueueOutOfRangeException
        else:
            self.items.append(value)
    @classmethod
    def FindQueue(cls,_Name):
        if _Name in cls.QueuesItems:
            return cls.QueuesItems[_Name]

    @classmethod
    def save(cls, filename):
        AllQueues=dict()
        for key,value in zip(cls.QueuesItems.keys(),cls.QueuesItems.values()):
            tempd=dict()
            tempd["size"]=value.Size
            tempd["items"] = value.items
            AllQueues[value.Name]=tempd
        with open(filename, 'w') as f:
            json.dump(AllQueues,f,indent=4)

    @classmethod
    def load(cls, filename):
        with open(filename,'r') as f:
            Data=json.load(f)
        for _name,_queue in zip (Data.keys(),Data.values()):
            tq=NamedQueue(_name,_queue['size'])
            tq.items=_queue['items']

'''nq=NamedQueue("Moamen",3)
nq.push(10)
nq.push(20)
nq.push(30)
nq.DisplayQueue()
nq.pop()
nq.pop()
nq.DisplayQueue()
nq2=NamedQueue("Mohamed",3)
nq2.push(40)
nq2.push(50)
nq3=NamedQueue("eltony",3)
nq3.push(60)
nq3.push(70)
nq4=NamedQueue.FindQueue("eltony")
nq4.DisplayQueue()
nq5=NamedQueue("abdltawab",10)

NamedQueue.save("Data.json")'''
NamedQueue.load("Data.json")
nq=NamedQueue.FindQueue("Mohamed")
nq.DisplayQueue()
new=NamedQueue('Mohamed',10)

