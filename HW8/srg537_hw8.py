import inspect
import sys

class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None
            self.nodeCount = 1

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    # raises exception if not found
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # returns None if not found
    def subtree_find_for_insert(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr.nodeCount += 1
                curr = curr.left
            else:  # (curr.item.key < key)
                curr.nodeCount += 1
                curr = curr.right
        return None

    def subtree_find_for_delete(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr.nodeCount -= 1
                curr = curr.left
            else:  # (curr.item.key < key)
                curr.nodeCount -= 1
                curr = curr.right
        return None

    def subtree_find(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                # curr.nodeCount += 1
                curr = curr.left
            else:  # (curr.item.key < key)
                # curr.nodeCount += 1
                curr = curr.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find_for_insert(self.root, key)
        if (node is None):
            self.subtree_insert(key, value)
        else:
            node.item.value = value

    # assumes key not in tree
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                curr = self.root.left
            else:
                curr = self.root.right
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    # curr.nodeCount += 1
                    curr = curr.left
                else:
                    # curr.nodeCount += 1
                    curr = curr.right
            if (key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.size += 1


    #raises exception if key not in tree
    def __delitem__(self, key):
        if (self.subtree_find(self.root, key) is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.subtree_delete(self.root, key)

    #assumes key is in tree + returns value assosiated
    def subtree_delete(self, node, key):
        node_to_delete = self.subtree_find(node, key)
        value = node_to_delete.item.value
        num_children = node_to_delete.num_children()

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root.nodeCount -= 1
                    self.root = self.root.left
                else:
                    self.root.nodeCount -= 1
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                self.root.nodeCount -= 1
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            self.root.nodeCount -= 1
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node = node.right
        return node

    def preorder(self):
        for node in self.subtree_preorder(self.root):
            yield node

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)

    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)
            # yield (node.item)

    def get_ith_smallest(self, i):
        # testing = (sys._getframe().f_back.f_code)
        # lines = inspect.getsourcelines(testing)
        # print("".join(lines[0]))

        if i > self.size:
            raise IndexError
        else:
            return self.smallSearch(self.root, i)

    def smallSearch (bst, node, i):

        if node.left is None and node.right is None:
            nodeCount = 1
        elif node.left is None:
            nodeCount = 0
        else:
            nodeCount = node.left.nodeCount


        if (node.left is None and i is 1):
            return node.item.key

        elif nodeCount + 1 is i:
            return node.item.key

        else:
            if i < nodeCount+1:
                return bst.smallSearch(node.left, i)

            else:
                return bst.smallSearch(node.right, (i-(nodeCount+1)))

def create_chain_bst(n):
    bst = BinarySearchTreeMap()

    for i in range(n+1):
        # item = BinarySearchTreeMap.Item(i)
        if i > 0:
            bst.subtree_insert(i)

    return bst

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    # if n is 1:
    #     bst.root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(n))
    #     return bst

    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    avg = (low + high) // 2

    # if n is 1:
    #     bst.root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(low))

    if low > high:
        return None

    else:
        # avg = (low+high)//2
        item = BinarySearchTreeMap.Item(avg)
        root = BinarySearchTreeMap.Node(item)
        root.left = add_items(10, low, avg-1)
        # root.right = add_items(10, (1+(low+high)//2), high)
        root.right = add_items(10, (1+avg), high)

    if (isinstance(bst, BinarySearchTreeMap)):
        bst.root = root

    else:
        return root

def restore_bst(prefix_lst):
    pos = 0
    tree = BinarySearchTreeMap()
    if (len(prefix_lst) is 0):
        return tree
    else:
        tree.root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[0]))
        tree.root = helper(prefix_lst, pos, prefix_lst[0], tree.root)[0]

        return tree

def helper(lst, pos, root, parent):

    if pos is len(lst)-1:
        return (BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[pos])), 0)

    else:
        curr = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[pos]))
        if lst[pos+1] < root:
            if (lst[pos+1] <= parent.item.key):
                pos += 1
                left = helper(lst, pos, root, curr)
                curr.left = left[0]
                pos = left[1]

            else:
                return (curr, pos)

            if lst[pos+1] > curr.item.key and lst[pos+1] < parent.item.key:
                right = helper(lst, pos+1, root, curr)
                curr.right = right[0]
                pos = right[1]

            if curr.item.key < root:
                return (curr, pos)

        if (lst[pos+1] > root and (lst[pos+1] < curr.item.key and lst[pos+1] > parent.item.key)):
            pos += 1
            left = helper(lst, pos, root, curr)
            curr.left = left[0]
            pos = left[1]

        if (curr.item.key >= root and lst[pos+1] >= parent.item.key):
            if parent.item.key <= curr.item.key and lst[pos+1] > curr.item.key:
                pos += 1
                right = helper(lst, pos, root, curr)
                curr.right = right[0]
                pos = right[1]

            # return (curr, right[1])
        if (curr.item.key >= root):
            return (curr, pos)

        return (curr, pos)


def find_min_abs_difference(bst):

    result = find_diff(bst.root, bst.root)
    return abs(result[0] - result[1])

def find_diff(node, parent):
    if (node.left is None and node.right is None):
        return (parent.item.key, node.item.key)

    if node.left is not None:
        left = find_diff(node.left, node)
    if node.right is not None:
        right = find_diff(node.right, node)
    if node.right is None:
        right = (parent.item.key, node.item.key)
    if node.left is None:
        left = (parent.item.key, node.item.key)

    diffChildren = right[1] - left[1]
    diffLeft = abs(left[0] - left[1])
    diffRight = abs(right[1] - right[0])
    minDiff = min(diffChildren, diffLeft, diffRight)

    if minDiff is diffChildren:
        return (right[1], left[1])
    if minDiff is diffLeft:
        return (left[0], left[1])
    if minDiff is diffRight:
        return (right[0], right[1])

# test = restore_bst([])
# for i in  test:
#     print(i)

# newTest = create_complete_bst(15)
# del newTest[9]
# for i in  newTest:
#     print(i)

bst = BinarySearchTreeMap()
bst[7] = None
bst[5] = None
bst[1] = None
bst[14] = None
bst[10] = None
bst[3] = None
bst[9] = None
bst[13] = None

test = BinarySearchTreeMap()
test.subtree_insert(50);
test.subtree_insert(30);
test.subtree_insert(20);
test.subtree_insert(40);

del test[50]
print(bst.get_ith_smallest(3))
print(bst.get_ith_smallest(6))

del bst[14]
del bst[5]
#
# # bst.assertEqual(bst.get_ith_smallest(3), 7)
# print(bst.get_ith_smallest(3))
# print(bst.get_ith_smallest(6))
# print(bst.get_ith_smallest(20))


# for node in bst.subtree_inorder(bst.root):
#     print(node.item)
#
# for i in bst:
#     print(i)