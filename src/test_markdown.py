import unittest
from markdown import(
    splitNodesDelimiter,
    extractMarkdownImages,
    #extractMarkdownLinks,
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
    def testExtractMarkdownImages(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        matches = extractMarkdownImages(text)
        self.assertEqual(
            [
                ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")
            ],
            matches,
        )
if __name__ == "__main__":
    unittest.main()