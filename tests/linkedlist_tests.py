from unittest import TestCase, TestLoader
from linkedlist import LinkedList

class ReverseTestCase(TestCase):
    def test_11rev_rec_nil(self):
        l = LinkedList()
        r = LinkedList()
        r.reverse(rec=True)
        self.assertEqual(r, l)

    def test_12rev_rec_single(self):
        l = LinkedList([1])
        r = LinkedList([1])
        r.reverse(rec=True)
        self.assertEqual(r, l)

    def test_13rev_rec_multiple(self):
        l = LinkedList([1, 2, 3])
        r = LinkedList([3, 2, 1])
        r.reverse(rec=True)
        self.assertEqual(r, l)

    def test_14rev_rec_twice(self):
        l = LinkedList([1, 2, 3])
        r = LinkedList([1, 2, 3])
        r.reverse(rec=True)
        r.reverse(rec=True)
        self.assertEqual(r, l)

    def test_21rev_loop_nil(self):
        l = LinkedList()
        r = LinkedList()
        r.reverse()
        self.assertEqual(r, l)

    def test_22rev_loop_single(self):
        l = LinkedList([1])
        r = LinkedList([1])
        r.reverse()
        self.assertEqual(r, l)

    def test_23rev_loop_multiple(self):
        l = LinkedList([1, 2, 3])
        r = LinkedList([3, 2, 1])
        r.reverse()
        self.assertEqual(r, l)

    def test_24rev_loop_twice(self):
        l = LinkedList([1, 2, 3])
        r = LinkedList([1, 2, 3])
        r.reverse()
        r.reverse()
        self.assertEqual(r, l)

suite = TestLoader().loadTestsFromTestCase(ReverseTestCase)