# for i in range(len(self)):
        #     d1 = temp1.l.delete(temp1.l.first_node())
        #     step1 = ord(d1[0])
        #     if not temp1.l.is_empty():
        #         step2 = ord(temp1.l.first_node().data[0])
        #     diffstep = (step2 - step1) ** 2
        #     # print(diffstep)
        #     sum1 += ord(d1[0]) * d1[1] + diffstep
        #     totalelem1 = d1[1] + totalelem1
        #
        # step1 = 0
        # step2 = 0
        # diffstep = 0
        #
        # # print("here")
        #
        # for i in range(len(other)):
        #     d1 = temp2.l.delete(temp2.l.first_node())
        #     step1 = ord(d1[0])
        #     if not temp2.l.is_empty():
        #         step2 = ord(temp2.l.first_node().data[0])
        #     diffstep = (step2 - step1) ** 2
        #     # print(diffstep)
        #     sum2 += ord(d1[0]) * d1[1] + diffstep
        #     totalelem2 += d1[1]
        #     # print(ord(d1[0]), d1[1], i, sum2)
        # avg1 = sum1 / totalelem1
        # avg2 = sum2 / totalelem2
    # def __le__(self, other):
    #     temp1 = CompactString(self.orig)
    #     temp2 = CompactString(other.orig)
    #     sum1 = 0
    #     totalelem1 = 0
    #     sum2 = 0
    #     totalelem2 = 0
    #     step1 = 0
    #     step2 = 0
    #     diffstep = 0
    #
    #     for i in range(len(self)):
    #         d1 = temp1.l.delete(temp1.l.first_node())
    #         step1 = ord(d1[0])
    #         if not temp1.l.is_empty():
    #             step2 = ord(temp1.l.first_node().data[0])
    #         else:
    #             step2 = step1
    #         diffstep = (step1 - step2)
    #         sum1 += ord(d1[0]) * d1[1] + (2**diffstep)
    #         print(diffstep, sum1)
    #         totalelem1 = d1[1] + totalelem1
    #
    #     print("here1")
    #     step1 = 0
    #     step2 = 0
    #     diffstep = 0
    #
    #     for i in range(len(other)):
    #         d1 = temp2.l.delete(temp2.l.first_node())
    #         step1 = ord(d1[0])
    #         if not temp2.l.is_empty():
    #             step2 = ord(temp2.l.first_node().data[0])
    #         else:
    #             step2 = step1
    #         diffstep = (step1 - step2)
    #         sum2 += ord(d1[0])*d1[1] + (2**diffstep)
    #         print(diffstep, sum2)
    #         totalelem2 += d1[1]
    #
    #
    #     print("here2")
    #
    #     avg1 = sum1 / totalelem1
    #     avg2 = sum2 / totalelem2
    #
    #     # print(sum2)
    #     print(avg1)
    #     print(avg2)
    #     return (avg1 <= avg2)
    #
    # def __gt__(self, other):
    #     return not (self <= other)
    #
    # def __ge__(self, other):
    #     return not (self < other)

    #
    # def __lt__(self, other):
    #     temp1 = CompactString(self.orig)
    #     temp2 = CompactString(other.orig)
    #     sum1 = 0
    #     totalelem1 = 0
    #     sum2 = 0
    #     totalelem2 = 0
    #     step1 = 0
    #     step2 = 0
    #     diffstep = 0
    #     for i in range(len(self)):
    #         d1 = temp1.l.delete(temp1.l.first_node())
    #         step1 = ord(d1[0])
    #         if not temp1.l.is_empty():
    #             step2 = ord(temp1.l.first_node().data[0])
    #         else:
    #             step2 = step1
    #         diffstep = (step1 - step2)
    #         if (diffstep > 0):
    #             sum1 += ord(d1[0]) * d1[1] + ((2**diffstep) * diffstep)
    #         else:
    #             sum1 += ord(d1[0]) * d1[1] + ((2**diffstep) * (diffstep*2))
    #         print(diffstep, sum1)
    #         totalelem1 = d1[1] + totalelem1
    #
    #     print("here1")
    #     step1 = 0
    #     step2 = 0
    #     diffstep = 0
    #
    #     for i in range(len(other)):
    #         d1 = temp2.l.delete(temp2.l.first_node())
    #         step1 = ord(d1[0])
    #         if not temp2.l.is_empty():
    #             step2 = ord(temp2.l.first_node().data[0])
    #         else:
    #             step2 = step1
    #         diffstep = (step1 - step2)
    #         if (diffstep > 0):
    #             sum2 += ord(d1[0]) * d1[1] + ((2**diffstep) * diffstep)
    #         else:
    #             sum2 += ord(d1[0]) * d1[1] + ((2**diffstep) * (diffstep*2))
    #         print(diffstep, sum2)
    #         totalelem2 += d1[1]
    #
    #     print("here2")
    #
    #     avg1 = sum1 / totalelem1
    #     avg2 = sum2 / totalelem2
    #
    #     # print(sum2)
    #     print(avg1)
    #     print(avg2)
    #
    #     return (avg1 < avg2)
    #
    #
    # def __le__(self, other):
    #     temp1 = CompactString(self.orig)
    #     temp2 = CompactString(other.orig)
    #     sum1 = 0
    #     totalelem1 = 0
    #     sum2 = 0
    #     totalelem2 = 0
    #     step1 = 0
    #     step2 = 0
    #     diffstep = 0
    #
    #     for i in range(len(self)):
    #         d1 = temp1.l.delete(temp1.l.first_node())
    #         step1 = ord(d1[0])
    #         if not temp1.l.is_empty():
    #             step2 = ord(temp1.l.first_node().data[0])
    #         diffstep = (step2 - step1)
    #         # print(diffstep)
    #         sum1 += ord(d1[0]) * d1[1]
    #         totalelem1 = ((ord(d1[0])/97) * d1[1]) + totalelem1
    #         print(totalelem1, sum1)
    #
    #     step1 = 0
    #     step2 = 0
    #     diffstep = 0
    #
    #     print("hi")
    #
    #     for i in range(len(other)):
    #         d1 = temp2.l.delete(temp2.l.first_node())
    #         step1 = ord(d1[0])
    #         if not temp2.l.is_empty():
    #             step2 = ord(temp2.l.first_node().data[0])
    #         diffstep = (step2 - step1)
    #         # print(diffstep)
    #         sum2 += ord(d1[0]) * d1[1]
    #         totalelem2 = ((ord(d1[0])/97) * d1[1]) + totalelem2
    #         print(totalelem2, sum2)
    #
    #     totalelem1 = truncate(totalelem1, 3)
    #     totalelem2 = truncate(totalelem2, 3)
    #     avg1 = float(sum1) / float(totalelem1)
    #     avg2 = sum2 / float(totalelem2)
    #
    #     print(avg1)
    #     print(avg2)
    #     print(totalelem1, sum1)
    #     print(totalelem2, sum2)
    #
    #     return (avg1 <= avg2)
    #
    # def deep(lnk_lst):
    #     result = DoublyLinkedList()
    #
    #     if (isinstance(lnk_lst, DoublyLinkedList)):
    #         now = lnk_lst.first_node()
    #         print("here")
    #         result = deep(now)
    #         return result
    #     else:
    #         now = lnk_lst
    #         print("here1")
    #         while now.data is not None:
    #             print(now.data)
    #             if (isinstance(now.data, int)):
    #                 result.add_last(now.data)
    #                 now = now.next
    #                 # result.add_last(deep_copy_linked_list(now.next))
    #             elif (isinstance(now.data, DoublyLinkedList)):
    #                 result = deep(now.data)
    #                 return result
    #         return result
    #
    # def deep2(lnk_lst):
    #     result = DoublyLinkedList()
    #     now = lnk_lst.first_node()
    #
    #     while now.data is not None:
    #         if (isinstance(now.data, int)):
    #             result.add_last(now.data)
    #             now = now.next
    #         elif (isinstance(now.data, DoublyLinkedList)):
    #             result.add_last(deep2(now.data))
    #             # now = now.next
    #             now = now.next
    #             # return result
    #
    #     return result