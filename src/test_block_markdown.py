import unittest
from markdown_blocks import (
    markdownToBlocks, 
    blockToBlockType,
    blockTypeCode,
    blockTypeParagraph,
    blockTypeHeading,
    blockTypeListOrdered,
    blockTypeListUnordered,
    blockTypeQuote,
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdownToBlocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with *italic* text and `code` here
            This is the same paragraph on a new line

            * This is a list
            * with items
            """
        blocks = markdownToBlocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdownToBlocks_newlines(self):
        md = """
        This is **bolded** paragraph




        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items
        """
        blocks = markdownToBlocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    def testblockToBlockType(self):
        block = "# heading"
        self.assertEqual(blockToBlockType(block), blockTypeHeading)
        block = "```\ncode\n```"
        self.assertEqual(blockToBlockType(block), blockTypeCode)
        block = "> quote\n> more quote"
        self.assertEqual(blockToBlockType(block), blockTypeQuote)
        block = "* list\n* items"
        self.assertEqual(blockToBlockType(block), blockTypeListUnordered)
        block = "1. list\n2. items"
        self.assertEqual(blockToBlockType(block), blockTypeListOrdered)
        block = "paragraph"
        self.assertEqual(blockToBlockType(block), blockTypeParagraph)

if __name__ == "__main__":
    unittest.main()