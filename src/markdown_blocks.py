blockTypeParagraph = "paragraph" #If nothing else
blockTypeListUnordered = "list" #Starts with * or -
blockTypeListOrdered = "list, ordered" #Number followed by .
blockTypeHeading = "heading" #Starts with 1 to 6 #'s
blockTypeQuote = "quotes" #Starts with >
blockTypeCode = "code" #Stats and ends with ```

def markdownToBlocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    print(filtered_blocks)
    return filtered_blocks

def blockToBlockType(block):
    lines = block.split("\n")
    if (
        block.startswith("# ")
        or block.startswith("##")
        or block.startswith("###")
        or block.startswith("####")
        or block.startswith("#####")
        or block.startswith("######")
    ):
        return blockTypeHeading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return blockTypeCode
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return blockTypeParagraph
        return blockTypeListUnordered
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return blockTypeParagraph
        return blockTypeListUnordered
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return blockTypeParagraph
            i += 1
        return blockTypeListOrdered
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return blockTypeParagraph
        return blockTypeQuote
    return blockTypeParagraph
    
    
blockTypeParagraph = "paragraph" #If nothing else

blockTypeQuote = "quotes" #Starts with >