INF = 99999 # INFINITY

# inputs
height = int(input('First, enter height of your tree:\n'))
arr = [ int(item) for item in input('Now, enter nodes from root to leaf (south to north and west to east)\n').split(' ')]

#Node
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.parent = None
        self.val = key 
        
#insert Array into a binary tree
def insertLevelOrder(arr, root, i, n): 
    if i < n: 
        temp = Node(arr[i])
        root = temp 
        root.right = insertLevelOrder(arr, root.right, 2 * i + 1, n)
        root.left = insertLevelOrder(arr, root.left, 2 * i + 2, n)
        if( i == 0 ):
            root.parent = -INF
        else:
            root.parent = arr[(i - 1) // 2 ]
    return root

#Find Local Maximum
def localMax(tree):
    if(tree.right is not None and tree.left is not None):
        if(tree.val > tree.right.val and tree.val > tree.left.val and tree.val > tree.parent ): #### tree.left.parent => tree.parent ####
            return tree.val
        else:
            if(tree.right.val < tree.left.val):
                return localMax(tree.left)
            else:
                return localMax(tree.right)
    else:
        return tree.val

#init and try to find in tree
tree = None
n = len(arr) 
tree = insertLevelOrder(arr, tree, 0, n)
localMaximum = localMax(tree)
print('\n----Answer----')
print('This is Local Maximum', localMaximum)
print('This is index of Local Maximum', arr.index(localMaximum)+1)