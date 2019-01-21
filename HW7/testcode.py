# exp = '* 2 + - 15 6 4'
# print(create_expression_tree(exp).root.right.right)

# r_l_ch1 = LinkedBinaryTree.Node(8)
# r_r_ch1 = LinkedBinaryTree.Node(4)
# r_ch2 = LinkedBinaryTree.Node(7, r_l_ch1, r_r_ch1)
#
# l_ch0 = LinkedBinaryTree.Node(5)
# r_ch0 = LinkedBinaryTree.Node(1)
# l_ch1 = LinkedBinaryTree.Node(9, l_ch0, r_ch0)
# l_ch2 = LinkedBinaryTree.Node(2, l_ch1)
# root = LinkedBinaryTree.Node(3, l_ch2, r_ch2)
# tree = LinkedBinaryTree(root)
#
# l = LinkedBinaryTree.Node(1)
# r = LinkedBinaryTree.Node(10)
# s2 = LinkedBinaryTree.Node(5, l, r)
# sample = LinkedBinaryTree(s2)
#
# single = LinkedBinaryTree(r)
# print(min_and_max(tree))

# n = LinkedBinaryTree()
# print(is_height_balanced(tree))
# print(n.leaves_list())






# for item in tree.preorder():
#     print(item)


# if (isinstance(left_height, bool)):
        #     return False
        # elif (isinstance(right_height, bool)):
        #     return False
        # else:
        #     diff = abs(left_height - right_height)
        #     if (diff is not 0 and diff is not 1):
        #         flag = False
        #         return flag
        #     else:
        #         return 1 + max(left_height, right_height)

# def hb(tree, node, flag):
#
#     if ((node is None)):
#         return 0
#     elif (node.left is None):
#         return 1 + hb(tree, node.right, flag)
#     elif (node.right is None):
#         return 1 + hb(tree, node.left, flag)
#     else:
#         left_height = (hb(tree, node.left, flag), flag)
#         right_height = (hb(tree, node.right, flag), flag)
#
#         if (isinstance(left_height, bool)):
#             return False
#         elif (isinstance(right_height, bool)):
#             return False
#         else:
#             diff = abs(left_height - right_height)
#             if (diff is not 0 and diff is not 1):
#                 flag = False
#                 return flag
#             else:
#                 return 1 + max(left_height, right_height)


