class node:
    def __init__(self, val):
        self.key = val
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def CommonAncestor(self,root, s1 ,s2):
        if root == None: return None
        elif root.key > s1 and root.key > s2:
            return self.CommonAncestor(root.left,s1,s2)
        elif root.key < s1 and root.key < s2:
            return self.CommonAncestor(root.right,s1,s2)
        return root

    def WalkPath(self,root, s1, arr):
        arr.append(root.key)
        if root.key == s1:
            return
        elif root.key < s1:
            self.WalkPath(root.right,s1,arr)
        else:
            self.WalkPath(root.left,s1,arr)
            

    def BinarySearch(self,val,root):
        if root == None:
            return 'NO ENCONTRADO'
        elif val == root.key:
            return root
        elif val <= root.key:
            return self.BinarySearch(val,root.left)
        else:
            return self.BinarySearch(val,root.right)

    def height(self, Node):
        if Node is None:
            return 0
        else:
            return Node.height

    def balance(self, Node):
        if Node is None:
            return 0
        else:
            return self.height(Node.left) - self.height(Node.right)

    def MinimumtitleNode(self, Node):
        if Node is None or Node.left is None:
            return Node
        else:
            return self.MinimumtitleNode(Node.left)

    def rotateR(self, Node):
        a = Node.left
        b = a.right
        a.right = Node
        Node.left = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def rotateL(self, Node):
        a = Node.right
        b = a.left
        a.left = Node
        Node.right = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def insert(self, val, root):
        if root is None:
            return node(val)
        elif val <= root.key:
            root.left = self.insert(val, root.left)
        elif val > root.key:
            root.right = self.insert(val, root.right)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        if balance > 1 and root.left.key > val:
            return self.rotateR(root)
        if balance < -1 and val > root.right.key:
            return self.rotateL(root)
        if balance > 1 and val > root.left.key:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if balance < -1 and val < root.right.key:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        return root

    def preorder(self, root):
        if root is None:
            return
        # print(root)
        if root.left != None: root.left.parent =root
        if root.right != None: root.right.parent = root
        self.preorder(root.left)
        self.preorder(root.right)

    def delete(self, val, Node):
        if Node is None:
            return Node
        elif val < Node:
            Node.left = self.delete(val, Node.left)
        elif val > Node:
            Node.right = self.delete(val, Node.right)
        else:
            if Node.left is None:
                lt = Node.right
                Node = None
                return lt
            elif Node.right is None:
                lt = Node.left
                Node = None
                return lt
            rgt = self.MinimumtitleNode(Node.right)
            Node = rgt
            Node.right = self.delete(rgt, Node.right)
        if Node is None:
            return Node
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        balance = self.balance(Node)
        if balance > 1 and self.balance(Node.left) >= 0:
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) <= 0:
            return self.rotateL(Node)
        if balance > 1 and self.balance(Node.left) < 0:
            Node.left = self.rotateL(Node.left)
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) > 0:
            Node.right = self.rotateR(Node.right)
            return self.rotateL(Node)
        return Node


def main():
    myTree= AVL()
    root = None
    N = int(input())
    for i in range(N):
        room = input()
        root = myTree.insert(room,root)
    myTree.preorder(root)
    K = int(input())
    for _ in range(K):
        A, B = tuple(input().split()) 
        ancestor = myTree.CommonAncestor(root,A,B)
        Apath = []
        Bpath = []
        myTree.WalkPath(ancestor,A,Apath)
        myTree.WalkPath(ancestor,B,Bpath)
        Apath = Apath[::-1]
        Apath = Apath[:len(Apath)-1]
        Apath = ','.join(Apath)
        Bpath = ','.join(Bpath)

        if Apath == '': 
            print(Bpath)
            continue
        elif Bpath == '':
            print(Apath)
            continue
        print(Apath+','+Bpath)


main()