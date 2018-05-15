

class LinkedList:
    nodesNumber = 0
    root = None

    class ListNode:
        value = None
        nextNode = None

    def createNode(self):
        self.nodesNumber += 1

        return self.ListNode()

    def insertNode(self, value):
        # build a root
        if self.root is None:
            self.root = self.createNode()
            self.root.value = value
            return

        # first point to the root
        current = self.root

        while True:
            # new value is less and we should insert it before current
            if value < current.value:
                newNode = self.createNode()

                # shift current node to the right
                newNode.value = current.value
                newNode.nextNode = current.nextNode

                current.value = value
                current.nextNode = newNode
                return

            if current.nextNode is None:
                current.nextNode = self.createNode()
                current.nextNode.value = value
                return

            # move to next node
            current = current.nextNode
        # end of while

    def median(self):
        if self.root is None:
            return 0

        N = self.nodesNumber
        N_2 = int(N/2)

        current = self.root
        if N%2 != 0:
            # go to the N/2 node
            for i in range(N_2):
                current = current.nextNode
            return current.value / 1.0

        # go to the N/2 - 1 node
        for i in range(N_2 - 1):
            current = current.nextNode

        firstMid = current.value
        secondMid = current.nextNode.value

        return (firstMid + secondMid) / 2.0

# this if for python list only
# def median(myList):
#     if myList is None:
#         return None
#
#     N = len(myList)
#     N_2 = int(N/2)
#
#     if N%2 != 0:
#         return myList[N_2] / 1.0
#
#     firstMid = myList[N_2]
#     secondMid = myList[N_2 - 1]
#
#     return (firstMid + secondMid) / 2.0

def insertSort(myList, value):
    index = 0
    for item in myList:
        if value <= item:
            break

        index += 1

    myList.insert(index, value)


if __name__ == "__main__":

    for i in range(9, 0, -1):
        print(i)
    N = int(input())

    # root
    myList = LinkedList()

    for i in range(N):
        value = int(input())
        myList.insertNode(value)
        print(myList.median())