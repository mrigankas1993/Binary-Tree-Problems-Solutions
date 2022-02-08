# TREE Free code camp 8/02/2022
from math import inf
class tree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class stack:
    def __init__(self):
        self.__storage = []
    def isempty(self):
        if len(self.__storage) == 0:
            return 'true'
        else:
            'false'
    def push(self, val2):
        self.__storage.append(val2)
    def pop(self):
        c = self.__storage.pop()
        return c
    def length(self):
        return len(self.__storage)
a = tree('a')
b = tree('b')
c = tree('c')
d = tree('d')
e = tree('e')
f = tree('f')
a.left = b
a.right = c
a.left.left = d
a.left.right = e
a.right.right = f
#1 Depth first search iterative version
def depth_first(node):
    STACK = stack()
    STACK.push(node)
    c = 1
    while c:
        current = STACK.pop()
        print(current.val)
        if current.right != None:
            STACK.push(current.right)
        if current.left != None:
            STACK.push(current.left)
        c = STACK.length()
depth_first(a)

#2 Depth first search recursive version
def recur_depth_first(node):
    if node == None:
        return []
    leftf = recur_depth_first(node.left)
    rightf = recur_depth_first(node.right)
    c = []
    c.extend(node.val)
    c.extend(leftf)
    c.extend(rightf)
    return c
print(recur_depth_first(a))

#3 Breath First search
def breath_first(node):
    queue = []
    queue.append(node)
    while len(queue) != 0:
        current = queue.pop(0)
        print(current.val)
        if current.right != None:
            queue.append(current.right)
        if current.left != None:
            queue.append(current.left)
breath_first(a)
#4 find if a particular value is in tree
def find_value(root, value):
    if root == None:
        return False
    if root.val == value:
        return True
    c = find_value(root.left, value) or find_value(root.right, value)
    return c
print(find_value(a, 'c'))

#5 tree sum 
'''                     20
                       /  \
                      11   53
                     /  \  / \
                    2    9 6  7
                          \
                           8
                          /
                        1000
                    '''

twenty = tree(20)
twenty.left = tree(11)
twenty.right = tree(53)
twenty.left.left = tree(2)
twenty.left.right = tree(9)
twenty.left.right.right = tree(8)
twenty.left.right.right.left = tree(1000)
twenty.right.left = tree(6)
twenty.right.right = tree(7)

#6 find the sum of all the nodes in a binary tree
def tree_sum(root):
    if root == None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)
print(tree_sum(twenty))

#7 find the sum of a sub tree with root node of main tree given along with value of the node who's sub tree sum is required
def sub_tree_sum(root1, value):
    if root1 == None:
        return 0
    if root1.val == value or value == True:
        return root1.val + sub_tree_sum(root1.left, True) + sub_tree_sum(root1.right, True)
    return sub_tree_sum(root1.left, 11) + sub_tree_sum(root1.right, 11)
print(sub_tree_sum(twenty, 11))



#8 Calculate the minimum value in a tree without min function
def tree_minimum(node):
    if node == None:
        return inf
    c = tree_minimum(node.left)
    d = tree_minimum(node.right)
    if c <= d:
        if c <= node.val:
            return c
        else:
            return node.val
    else:
        if d <= node.val:
            return d
        else:
            return node.val
            

#9 Calculate the minimum value in a tree with min function

def tree_min(node):
    if node == None:
        return inf
    return min(node.val, tree_min(node.left), tree_min(node.right))
print(tree_min(twenty))


#10 find all the leaf nodes
def find_leaf(node):
    if node == None:
        return []
    d = find_leaf(node.left)
    length1 = len(d)
    if length1 == 0:
        if node.right == None:
            d.append(node.val)
    e = find_leaf(node.right)
    length2 = len(e)
    if length2 == 0:
        if length1 != 0:
            if node.left == None:
                e.append(node.val)
    d.extend(e)
    return d
print(find_leaf(twenty))


#11 Find the max path sum from root to leaf
def max_path_sum(node):
    if node == None:
        return 0
    c = max_path_sum(node.left)
    if c == 0:
        c = node.val
    else:
        c += node.val
    d = max_path_sum(node.right)
    if d == 0:
        d = node.val
    else:
        d += node.val
    return max(c,d)
print(max_path_sum(twenty))




        

        
    
    

    


        
    


    
    
    

    
    






    
    





        
    



        

            
        
        











    
    
