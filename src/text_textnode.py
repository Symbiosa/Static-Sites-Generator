import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("Node is text", "italic", url=None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()