import random

class Queue:
    """
    A FIFO (first-in, first-out) queue backed by a Python list.

    The front of the queue is index 0 and the back is the end of the list,
    so entries are processed in the order they were received.
    """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.

        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        # pop(0) shifts the remaining items left, so this is O(n). That's fine
        # for a raffle-sized queue; collections.deque would make it O(1).
        return self.items.pop(0)

    def peek(self):
        """
        Return the item at the front of the queue without removing it.

        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        """Return True if the queue has no items."""
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.

        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("cannot select a winner from an empty queue")

        # Pick the winner by position rather than by name, so the right entry
        # is chosen even if two customers share the same name.
        winner_position = random.randrange(len(self.items))

        # Honor FIFO order: everyone ahead of the winner is processed (dequeued)
        # first, and the last item dequeued is the winner.
        for _ in range(winner_position + 1):
            winner = self.dequeue()

        print(
            f"Winner: {winner}! "
            f"Processed {winner_position + 1} entries; {len(self.items)} still in line."
        )
        return winner


if __name__ == "__main__":
    raffle = Queue()
    for i in range(1, 11):
        raffle.enqueue(f"Customer #{i}")

    print(f"Entries received: {raffle.items}")
    print(f"First in line:    {raffle.peek()}")
    raffle.select_and_announce_winner()
    print(f"Remaining:        {raffle.items}")
