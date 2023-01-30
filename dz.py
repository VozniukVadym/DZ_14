class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
                                                # Медод формування дерева
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

                                                #Метод максимального елеманта
    def maks(self):
        if self.right:
            self.right.maks()
            return
        print('Max - ',self.data)
                                                #Метод знаходження мінімального елеманта
    def minn(self):
        if self.left:
            self.left.minn()
            return
        print('Min - ',self.data)
                                                #Виведення дерева
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def find(self,node, parent, value):
        if node is None:
            return None, parent, False
        if value == node.data:
            return node, parent, True
        if value<node.data:
            if node.left:
                return self.find(node.left,node,value)
        if value > node.data:
            if node.right:
                return self.find(node.right, node, value)
        return None, parent, False

    def del_one_child(self,s,p):                                #видалення елемента з одним
        if p.left==s:
            if s.left is None:
                p.left=s.right
            elif s.right is None:
                p.left=s.left
        elif p.right==s:
            if s.left is None:
                p.right=s.right
            elif s.right is None:
                p.right=s.left

    def del_leaf(self, s,p):                                    #видалення листового елемента
        if p.left==s:
            p.left=None
        elif p.right==s:
            p.right=None

    def find_min(self,node, parent):
        if node.left:
            self.find_min(node.left, node)
        return node, parent

    def del_node(self,key):

        s, p, fl_find = self.find(root, None, key)

        if not fl_find:
            return None
        if s.left==None and s.right==None:
            self.del_leaf(s,p)
        elif s.left is None or s.right is None:
            self.del_one_child(s,p)
        else:
            sr, pr =self.find_min(s.right,s)
            s.data=sr.data
            self.del_one_child(sr, pr)

x=[14,35,10,50,19,31,42]

root = Node(27)
for i in x:
    root.insert(i)

root.PrintTree()
root.maks()
root.minn()

root.del_node(14)

root.PrintTree()
