import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "www.hyvinvointvarkkaja.fi")
        node2 = TextNode("Node is text", "italic", url=None)
        node3 = TextNode("String", "Kissa", url = False)
        node4 = TextNode(self,self,url = self)
        self.assertEqual(node, node2)
        self.assertEqual(node,node3)
        self.assertEqual(node,node4)

if __name__ == "__main__":
    unittest.main()