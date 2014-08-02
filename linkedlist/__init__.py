class LinkedList(object):
    """Python implementation of a singly-linked list"""

    def __init__(self, list_init=[]):
        """
        Initializes a LinkedList.

        Keyword arguments:
        list_init -- initialize the LinkedList with a normal Python list
        """

        # Every node in the LinkedList is a pair of (value, nextNode)
        agg = None
        for e in list_init[::-1]:
            agg = (e, agg)
        self._head = agg

    def reverse(self, rec=False):
        """
        Reverses the LinkedList.

        Keyword arguments:
        rec -- if True, uses the recursive implementation, otherwise the iterative one
        """

        # Short-circuit for trivial cases (empty and one-element)
        if self._head is None or self._head[1] is None:
            return

        # Choosing between the implementations
        fold = self._fold_rec if rec else self._fold_loop

        # Using fold to reverse the list
        self._head = fold(lambda *x: tuple(x), None, self._head)

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
         self._head) + "None]"
    
    def __eq__(self, other):
        next1 = self._head
        next2 = other._head
        while None not in [next1, next2]:
            (val1, next1) = next1
            (val2, next2) = next2
            if val1 != val2:
                return False
        if next1 == next2:
            return True
        return False