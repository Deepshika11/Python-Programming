class node:
    def __init__(self,item):
        self.info=item
        self.link=None


class LinkedList:
    def __init__(self,item):
        self.start=node(item)

    def insert_at_last(self,item):
        n=node(item)
        t=self.start
        while t.link!=None:
            t=t.link
        t.link=n
       

    def insert_at_beginning(self,item):
        n=node(item)
        n.link=self.start
        self.start=n


    #Insert after Specific item:
    def insert_at_specific1(self,item,after):
        n=node(item)
        t=self.start
        while t!=None and t.info!=after:
            t=t.link
        n.info=item
        n.link=t.link
        t.link=n

    #Insert in a Specific Position:
    def insert_at_specific2(self,item,index):
        n=node(item)
        t=self.start
        p=1
        while p<index-1 and t!=None:
            t=t.link
            p+=1
        n.link=t.link
        t.link=n

    def delete_at_last(self):
        t=self.start
        while t.link!=None:
            prev=t
            t=t.link
        del(t)
        prev.link=None

    def delete_at_beginning(self):
        t=self.start
        self.start=t.link
        del(t)


    #Delete after a Specific item:
    def delete_at_specific1(self,item):
        t=self.start
        if t.info==item:
            self.start=self.start.link
            del(t)
            print("\n Item deleted.")
        else:
            flag=0
            while t.link !=None and t.info!=item:
                prev = t
                t = t.link
                if t.info==item:
                    flag=1
            
            if flag==1:
                prev.link=t.link
                del(t)
                print("\nItem deleted.")
            else:
                print("\n Item not found.")
                


    #Delete at Specific index:
    def delete_at_specific2(self,index):
        t=self.start
        if index==1 or index==0:
            self.start = self.link
            del(t)
            print("\n deleted from the reqd positipn.")

        else:
            count=1
            while t.link!=None and count!=index:
                prev=t
                t=t.link
                count+=1
            if index>count:
                print("\n Invalid index {count}")
            else:
                prev.link=t.link
                del(t)
                print("\n deleted from the reqd positipn.")


    
    def traverse(self):
        t=self.start
        while t!=None:
            print(t.info)
            t=t.link
    


ob1=LinkedList(12)

print("Inserting at last: ")
ob1.insert_at_last(45)
ob1.insert_at_last(41)
ob1.insert_at_last(25)
ob1.traverse()

print("\nInserting in the beginning: ")
ob1.insert_at_beginning(50)
ob1.traverse()

print("\nInserting after a specific node: ")
ob1.insert_at_specific1(11,41)
ob1.traverse()

print("\nInserting at specific pos: ")
ob1.insert_at_specific2(10,3)
ob1.traverse()

print("\nDeleting at last :")
ob1.delete_at_last()
ob1.traverse()

print("\nDeleting at beg :")
ob1.delete_at_beginning()
ob1.traverse()

print("\nDeleting a specific node :")
ob1.delete_at_specific1(41)
ob1.traverse()

print("\nDeleting at specific pos :")
ob1.delete_at_specific2(3)
ob1.traverse()
