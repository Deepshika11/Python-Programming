class Node:
    def __init__(self, item):
        self.info = item
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    # insert --------------
    def insert(self, item):
        n = Node(item)
        if self.root == None:
            self.root = n
            return
        t = self.root
        while(t != None):
            par = t
            if n.info <= t.info:
                t = t.left
            else:
                t = t.right
        if n.info <= par.info:
            par.left = n
        else:
            par.right = n 

    # inorder ------------
    def inorder(self, R):
        if R != None:
            self.inorder(R.left)
            print(R.info, end=" ")
            self.inorder(R.right)

    # preorder ------------
    def preorder(self, R):
        if R != None:
            print(R.info, end=" ")
            self.preorder(R.left)
            self.preorder(R.right)

    # postorder -------------
    def postorder(self, R):
        if R != None:
            self.postorder(R.left)
            self.postorder(R.right)
            print(R.info, end=" ")

l = BST()
while(True):
    print("\n\n<<--- Binary Search Tree --->>")
    print("  1. Insert node")
    print("  2. Inorder")
    print("  3. Preorder")
    print("  4. Postorder\n")

    ch = int(input("Enter your choice :"))
    if ch == 1:
        n = int(input("Enter your value: "))
        l.insert(n)

    elif ch == 2:
        print("Your inorder traverse is: ")
        l.inorder(l.root)
    elif ch == 3:
        print("Your preorder traverse is: ")
        l.preorder(l.root)
    elif ch == 4:
        print("Your postorder traverse is: ")
        l.postorder(l.root)
    else:
        print("Invalid Input")

