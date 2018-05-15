from unittest import TestCase
import listMedian

class TestInsertList(TestCase):
    def testInsertSort(self):
        myList = []

        listMedian.insertSort(myList, 10)
        listMedian.insertSort(myList, 4)
        listMedian.insertSort(myList, 1)
        listMedian.insertSort(myList, 11)

        self.assertEqual(myList, [1, 4, 10, 11])

    def testInsertNode(self):
        myList = listMedian.LinkedList()

        myList.insertNode(10)
        myList.insertNode(4)
        myList.insertNode(1)
        median = myList.median()
        self.assertEqual(median, 4)

        myList.insertNode(11)
        median = myList.median()
        self.assertEqual(median, 7.0)

        self.assertEqual(myList.nodesNumber, 4)
        current = myList.root
        self.assertEqual(current.value, 1)
        current = current.nextNode
        self.assertEqual(current.value, 4)
        current = current.nextNode
        self.assertEqual(current.value, 10)
        current = current.nextNode
        self.assertEqual(current.value, 11)