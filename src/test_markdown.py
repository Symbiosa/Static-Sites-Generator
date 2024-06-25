import unittest
from markdown import(
    splitNodesDelimiter,
)

from textnode import (
    TextNode,
    textTypeText,
    textTypeBold,
    textTypeItalic,
    textTypeCode,
)

class testMarkdown(unittest.TestCase):
    def testDelimBold(self):
        node = TextNode("This is text with a **bolded** word", textTypeText)
        newNodes = splitNodesDelimiter([node], "**", textTypeBold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", textTypeText),
                TextNode("bolded", textTypeBold),
                TextNode(" word", textTypeText),
            ],
            newNodes,
        )

    def testDelimBoldDouble(self):
        node = TextNode("This is text with **bolded** and **bolder** words",textTypeText)
        newNodes = splitNodesDelimiter([node],"**", textTypeBold)
        self.assertListEqual(
            [
                TextNode("This is text with ", textTypeText),
                TextNode("bolded", textTypeBold),
                TextNode(" and ",textTypeText),
                TextNode("bolder", textTypeBold),
                TextNode(" words", textTypeText),
            ],
            newNodes,
        )
        
if __name__ == "__main__":
    unittest.main()