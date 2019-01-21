tItem = BinarySearchTreeMap.Item(10)
tNode = BinarySearchTreeMap.Node(tItem)
test = BinarySearchTreeMap()
test.root = tNode

for i in  test:
    print(i)

# test = create_chain_bst(4)

test = restore_bst([9,7,3,1,5,20,11,25])
for i in  test:
    print(i)

print(find_min_abs_difference(test))
# print(min(1,5,4))
# print(test.root.right.right.parent.item.key)
# print((1+7)//2)

# newTest = create_complete_bst(7)
# for i in  newTest:
#     print(i)

    # if (parent.item.key - left[0] < left[0] - left[1]):
    #     left = (parent.item.key, left[0])
    # else:
    #     left = (left[0], left[1])

bst = BinarySearchTreeMap()
bst[7] = None
bst[5] = None
bst[1] = None
bst[14] = None
bst[10] = None
bst[3] = None
bst[9] = None
bst[13] = None

# bst[8] = None
# for node in bst.subtree_inorder(bst.root):
#     print(node.item)

for i in bst:
    print(i)

print(bst.get_ith_smallest(7))
# print(bst.root.right.nodeCount)
