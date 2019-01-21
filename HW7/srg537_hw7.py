class EmptyTree(Exception):
    pass

class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self
            self.parent = None

        def __str__(self):
            # print("sheep")
            return str(self.data)

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def subtree_count(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return left_count + right_count + 1


    def sum_tree(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return left_sum + right_sum + subtree_root.data

    def height(self):
        if (self.root is None):
            raise EmptyTree("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    #assuming subtree_root is not empty
    def subtree_height(self, subtree_root):
        if((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif(subtree_root.left is None):
            return 1 + self.subtree_height(subtree_root.right)
        elif(subtree_root.right is None):
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)

    def printTree(self):
        if (self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if (node != None):
            self._printTree(node.left)
            print (str(node.data) + ' ')
            self._printTree(node.right)
    def leaves_list(self):
        result = []

        if (self.root is None):
            return result
            # raise EmptyTree("EmptyTree")
        else:
            return leaves(self, self.root, result)

    def iterative_inorder(self):
        if (self.root is None):
            # raise EmptyTree("EmptyTree")
            return None
        else:
            node = self.root
            is_left_finished = False

            while node is not None:
                # print("sheep")
                if is_left_finished is False:
                    while (node.left is not None):
                        node = node.left
                    is_left_finished = True

                yield node.data

                if node.right is not None:
                    is_left_finished = False
                    node = node.right
                else:
                    if node.parent is None:
                        break
                    if(node.parent.left is node):
                        node = node.parent
                    else:
                        while(node.parent.right is node):
                            node = node.parent
                            if node.parent is None:
                                break
                        node = node.parent

def min_and_max(bin_tree):
    def subtree_min_and_max(bin_tree, subtree_root):
        left = 0
        right = 0
        min = 0
        max = 0

        if subtree_root is None:
            return None

        elif subtree_root.left is None and subtree_root.right is None:
            return subtree_root.data
        # elif isinstance(subtree_root.left, LinkedBinaryTree.Node()):

        else:
            left = subtree_min_and_max(bin_tree, subtree_root.left)
            right = subtree_min_and_max(bin_tree, subtree_root.right)
            if(isinstance(left, int) and isinstance(right, int)):
                if left < right:
                    max = right
                    min = left

                else:
                    max = left
                    min = right

            elif(isinstance(left, tuple) and isinstance(right, int)):
                if right < left[0]:
                    min  = right
                    max = left[1]
                elif right > left[1]:
                    max = right
                    min = left[0]
                else:
                    min = left[0]
                    max = left[1]

            elif (isinstance(right, tuple) and isinstance(left, int)):
                if left < right[0]:
                    min = left
                    max = right[1]
                elif left > right[1]:
                    max = left
                    min = right[0]
                else:
                    min = right[0]
                    max = right[1]

            else:
                if (right is None):
                    max = left[1]
                    min = left[0]
                elif (left is None):
                    max = right[1]
                    min = right[0]

                else:
                    if left[0] < right[0]:
                        min = left[0]
                    else:
                        min = right[0]

                    if left[1] < right[1]:
                        max = right[1]
                    else:
                        max = left[1]

            if (subtree_root.data > max):
                max = subtree_root.data
            elif(subtree_root.data < min):
                min = subtree_root.data
            return (min, max)

        # return (min, max)

    if (bin_tree.root is None):
        raise EmptyTree("EmptyTree")
    else:
        result = subtree_min_and_max(bin_tree, bin_tree.root)
        if (isinstance(result, int)):
            return (result, result)
        else:
            return result

def leaves(self, subtree_root, result):
    if subtree_root is None:
        return None
    elif subtree_root.left is None and subtree_root.right is None:
        result.append(subtree_root.data)
    else:
        left = leaves(self, subtree_root.left, result)
        right = leaves(self, subtree_root.right, result)

    return result

def is_height_balanced(bin_tree):
    flag = True
    if (bin_tree.root is None):
        raise EmptyTree("EmptyTree")
    else:
        flag =  test(bin_tree, bin_tree.root, flag)
        return flag[1]
        # if flag is not False:
        #     return True
        # return hb(bin_tree, bin_tree.root, flag)


def test(tree, node, flag):
    if ((node is None)):
        return (0,True)
    elif (node.right is not None and node.left is not None):
        left_height = test(tree, node.left, flag)
        right_height = test(tree, node.right, flag)

        if left_height[1] is True and right_height[1] is True:
            diff = abs(left_height[0] - right_height[0])
            if (diff is not 0 and diff is not 1):
                flag = False
                return (1 + max(left_height[0], right_height[0]), flag)
            else:
                return (1 + max(left_height[0], right_height[0]), flag)
        else:
            if left_height[1] is False or right_height[1] is False:
                flag = False
            return (1 + max(left_height[0], right_height[0]), flag)

    elif (node.left is None):
        right_height = test(tree, node.right, flag)

        if (right_height[0] is not 0 and right_height[0] is not 1):
            flag = False

        return (1 + right_height[0], flag)

    else:
        left_height = test(tree, node.left, flag)
        if (left_height[0] is not 0 and left_height[0] is not 1):
            flag = False

        return (1 + left_height[0], flag)




def create_expression_tree(prefix_exp_str):
    list = prefix_exp_str.split(" ")
    start = 0
    space = 0

    lst = []
    for i in list:
        if i is '*' or i is '+' or i is '-' or i is '/':
            lst.append(i)
        else:
            x = int(i)
            lst.append(x)
    # return lst
    # tree = 0
    # tree = ex(lst, start)
    tree = LinkedBinaryTree(ex(lst, start)[0])

    return tree

def ex(lst, start):
    c = lst[start]
    if (isinstance(c, int)):
        return (LinkedBinaryTree.Node(c), start)
    else:
        root = LinkedBinaryTree.Node(c)
        sheep = ex(lst, start+1)
        root.left = sheep[0]
        newI = sheep[1]
        root.right = ex(lst, newI+1)[0]
        # print("here")
        return (root, newI+1)
    return root

def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    result = []

    def prefix_to_postfix_helper(tree, node):
        if node is None:
            return None

        elif node.left is None and node.right is None:
            result.append(node.data)
        else:
            prefix_to_postfix_helper(tree, node.left)
            prefix_to_postfix_helper(tree, node.right)
            result.append(node.data)

            return result

    prefix_to_postfix_helper(tree, tree.root)

    postfix_exp = ""

    for i in range(len(result)):
        postfix_exp += str(result[i])
        if i is not len(result) -1:
            postfix_exp += " "

    return postfix_exp

exp = '* 2 + - 15 6 4'
print(create_expression_tree(exp).root.right.right)
print(prefix_to_postfix(exp))
r_l_ch1 = LinkedBinaryTree.Node(8)
r_r_ch1 = LinkedBinaryTree.Node(4)
r_ch2 = LinkedBinaryTree.Node(7, r_l_ch1, r_r_ch1)

l_ch0 = LinkedBinaryTree.Node(5)
r_ch0 = LinkedBinaryTree.Node(1)
l_ch1 = LinkedBinaryTree.Node(9, l_ch0, r_ch0)
l_ch2 = LinkedBinaryTree.Node(2, l_ch1)
root = LinkedBinaryTree.Node(3, l_ch2, r_ch2)
tree = LinkedBinaryTree(root)

l = LinkedBinaryTree.Node(1)
r = LinkedBinaryTree.Node(10, LinkedBinaryTree.Node(6))
s2 = LinkedBinaryTree.Node(5, l, r)
sample = LinkedBinaryTree(s2)

single = LinkedBinaryTree(r)
print(min_and_max(tree))

n = LinkedBinaryTree()
print(is_height_balanced(tree))
print(n.leaves_list())


for t in tree.iterative_inorder():
    print(t, end = ' ')
print()


def sheep (self):
    node = self.root

    return peep2(node)

def peep (node):
    if node.left is None and node.right is None:
        return [1,0,0]
    elif(node.right and node.left is not None):
        right = peep(node.right)
        left = peep(node.left)
        total = [0,0,1]
        total[0]  += right[0] + left[0]
        total[1]  += right[1] + left[1]
        total[2]  += right[2] + left[2]
        return total
    elif (node.right is None):
        total = peep(node.left)
        total[1] += 1
        return total
    else:
        total = peep(node.right)
        total[1] += 1
        return total

def peep2 (node):
    if node is None:
        return [1,0,0]
    elif(node.right or node.left is not None):
        right = peep2(node.right)
        left = peep2(node.left)
        total = [0,0,1]
        total[0]  += right[0] + left[0]
        total[1]  += right[1] + left[1]
        total[2]  += right[2] + left[2]
        return total

# print(sheep(sample))

def depth (k, root):
    if k is 0:
        return 1
    else:
        right = 0
        if root.right is not None:
            right = depth(k-1, root.right)

        left = 0
        if root.left is not None:
            left = depth(k-1, root.left)

        return (left + right)

# print(depth(3, tree.root))

# print((None < 2 or None is not 2))
def m (node):
    if node.right is None and node.left is None:
        return (node.data,node.data)
    elif node.right and node.left is not None:
        right = m(node.right)
        left = m(node.left)
        return (min(right[0], left[0], node.data), max(left[1], right[1], node.data))
    elif (node.right is not None):
        right = m(node.right)
        if node.data < right[0]:
            right[0] = node.data
        elif node.data > right[1]:
            right[1] = node.data
        return right
    else:
        left = m(node.left)
        if node.data < left[0]:
            left[0] = node.data
        elif node.data > left[1]:
            left[1] = node.data
        return left


def m2 (node):
    if node.right is None and node.left is None:
        return (node.data, node.data)
    else:
        right = m2(node.right)
        left = m2(node.left)
        return (min(right[0], left[0], node.data), max(left[1], right[1], node.data))


# print(m2(tree.root))
