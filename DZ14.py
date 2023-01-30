class Tree:
    def __init__(self, id_node):
        self.id_node=id_node
        self.left=None
        self.right=None

    def __str__(self):
        return f'Node{self.id_node}, left {self.left}, right{self.right}'

    def insert(self, id_node):
        if self.id_node==id_node:
            return
        if self.id_node>id_node:
            if self.left==None:
                self.left=Tree(id_node)
            else:
                self.left.insert(id_node)
        elif self.id_node<id_node:
            if self.right==None:
                self.right=Tree(id_node)
            else:
                self.right.insert(id_node)

    def min_max(self, node):
        if node:
            print(node.id_node)
            min_max(node.left)
            min_max(node.right)



lst = [18,7,12,18,12,5,100]
node = Tree(lst[0])
for x in lst:
    node.insert(x)
print(node)
node.min_max(18)

