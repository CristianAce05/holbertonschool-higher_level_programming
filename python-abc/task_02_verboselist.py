#!/usr/bin/python3
"""VerboseList class that extends Python's list with notifications."""

class VerboseList(list):
    """List subclass that prints messages on modifications."""

    def append(self, item):
        """Add an item to the list and notify."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend the list with an iterable and notify."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        """Remove an item from the list and notify."""
        if item in self:
            super().remove(item)
            print(f"Removed {item} from the list.")
        else:
            raise ValueError(f"{item} not in list")

    def pop(self, index=-1):
        """Pop an item from the list and notify."""
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item


# --- Example usage ---
if __name__ == "__main__":
    vlist = VerboseList()

    vlist.append(10)                # Added 10 to the list.
    vlist.extend([20, 30, 40])      # Extended the list with 3 items.
    vlist.remove(20)                # Removed 20 from the list.
    popped_item = vlist.pop()       # Popped 40 from the list.
    popped_item = vlist.pop(0)      # Popped 10 from the list.
