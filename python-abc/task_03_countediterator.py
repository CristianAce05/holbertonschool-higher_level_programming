#!/usr/bin/python3
"""CountedIterator class that wraps an iterator and counts items iterated."""

class CountedIterator:
    """Iterator wrapper that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and a counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """Return the next item and increment the counter."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            # Re-raise StopIteration when no more items
            raise

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.counter

    def __iter__(self):
        """Iterator's __iter__ returns self."""
        return self


# --- Example usage ---
if __name__ == "__main__":
    data = [10, 20, 30, 40]
    counted_iter = CountedIterator(data)

    print("Iterating manually:")
    print(next(counted_iter))  # 10
    print(next(counted_iter))  # 20
    print("Count so far:", counted_iter.get_count())  # 2

    print("\nIterating in a loop:")
    for item in counted_iter:
        print(item)  # 30, 40

    print("Total count:", counted_iter.get_count())  # 4
