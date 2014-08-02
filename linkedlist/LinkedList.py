from operator import concat

class LinkedList(object):
    """Python implementation of a singly-linked list"""

    def __init__(self, list_init=None):
        """
        Initializes a LinkedList.

        Keyword arguments:
        list_init -- initialize the LinkedList with a normal Python list
        """

        # Every node in the LinkedList is a pair of (value, nextNode)
        agg = None
        for e in list_init[::-1]:
            agg = (e, agg)
        self.head = agg

    def reverse(self, rec=False):
        """
        Reverses the LinkedList.

        Keyword arguments:
        rec -- if True, uses the recursive implementation, otherwise the iterative one
        """

        # Short-circuit for trivial cases (empty and one-element)
        if self.head is None or self.head[1] is None:
            return

        # Choosing between the implementations
        fold = self._fold_rec if rec else self._fold_loop

        # Using fold to reverse the list
        self.head = fold(lambda *x: tuple(x), None, self.head)

    @classmethod
    def _fold_rec(cls, f, agg, next):
        """Tail-recursive implementation of fold"""

        if next is None:
            return agg
        (val, next) = next
        return cls._fold_rec(f, f(val, agg), next)

    @classmethod
    def _fold_loop(cls, f, agg, next):
        """Interative implementation of fold"""

        while next is not None:
            (val, next) = next
            agg = f(val, agg)
        return agg

    def __str__(self):
        """Reusing fold in order to generate the string representation"""

        return self._fold_loop(lambda x, y: y + "%s -> " % x, "LinkedList [",\
         self.head) + "None]"