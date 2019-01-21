def maxInLinked(lnk_lst):
    return max_subList(lnk_lst, lnk_lst.firstnode())

def max_sublist(lnk_lst, sublist_head):
    if (sublist_head is lnk_lst.last_node.node()):
        return sublist_head.data
    else:
        rest_max = max_sublist()
        if (rest_max > sublist_head.data):
            return rest_max
        else:
            return sublist_head.data