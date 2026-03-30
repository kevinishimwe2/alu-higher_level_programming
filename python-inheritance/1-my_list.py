#!/usr/bin/python3
"""Module that defines MyList, a subclass of list with a print_sorted method."""


class MyList(list):
    """A class that inherits from list and adds a sorted print method."""

    def print_sorted(self):
        """Print the list in ascending sorted order without modifying the original."""
        print(sorted(self))
