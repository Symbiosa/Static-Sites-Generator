from textnode import (
    TextNode,
    textTypeText,
    textTypeBold,
    textTypeItalic,
    textTypeCode
)
import re
import os
import markdown2  # Assuming markdown2 for markdown to HTML conversion, e.g., 'pip install markdown2'

def textToTextnodes(text):
    #creating tuple nodes with TextNode object inside, adding more to the tuple everytime we split
    nodes = [TextNode(text, textTypeText)]
    #splitting TextNode object with splitNodesDelimiter, ** Bold **
    print(nodes)
    nodes = splitNodesDelimiter(nodes,"**",textTypeBold)
    print(nodes)
    #splitting TextNode object with splitNodesDelimiter, * Italic * 
    nodes = splitNodesDelimiter(nodes,"*", textTypeItalic)
    print(nodes)
    #splitting TextNode object with splitNodesDelimiter, ` Code `
    nodes = splitNodesDelimiter(nodes,"`", textTypeCode)
    print(nodes)
    #splitting TextNode object with splitNodesImage
    nodes = splitNodesImage(nodes)
    print(nodes)
    #splitting TextNode object with splitNodesLink
    nodes = splitNodesLink(nodes)
    print(nodes)
    for node in nodes:
        #printting each object one by one to test function and if it go split corretly
        print(TextNode.__repr__(node))
    return nodes

def splitNodesDelimiter(oldNodes, delimiter, textType):
    nodeList = []
    for oldNode in oldNodes:
        if oldNode.textType != textTypeText:
            nodeList.append(oldNode)
            continue
        splitNodes = []
        sections = oldNode.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                splitNodes.append(TextNode(sections[i], textTypeText))
            else:
                splitNodes.append(TextNode(sections[i], textType))
        nodeList.extend(splitNodes)
    return nodeList

def splitNodesImage(oldNodes):
    nodeList = []
    for oldNode in oldNodes:
        try:
            
            images = extractMarkdownImages(oldNode.text)
            
            if not images:
                raise ValueError("No images found")
            
            currentText = oldNode.text
            for imageTup in images:
                before, after = currentText.split(f"![{imageTup[0]}]({imageTup[1]})",1)
                
                if before:
                    nodeList.append(TextNode(before, oldNode.textType))
                    
                nodeList.append(TextNode(imageTup[0], "text_type_image", imageTup[1]))

                currentText = after
            if currentText:
                nodeList.append(TextNode(currentText, oldNode.textType))
        except ValueError:
            nodeList.append(oldNode)
            continue  
    return nodeList
    
def splitNodesLink(oldNodes):
    nodeList = []
    for oldNode in oldNodes:
        try:
            
            links = extractMarkdownLink(oldNode.text)
            
            if not links:
                raise ValueError("No links found")
            
            currentText = oldNode.text
            for linkTup in links:
                before, after = currentText.split(f"[{linkTup[0]}]({linkTup[1]})",1)
                
                if before:
                    nodeList.append(TextNode(before, oldNode.textType))
                    
                nodeList.append(TextNode(linkTup[0], "textTypeLink", linkTup[1]))

                currentText = after
            if currentText:
                nodeList.append(TextNode(currentText, oldNode.textType))
        except ValueError:
            nodeList.append(oldNode)
            continue  
    return nodeList
    
    
def extractMarkdownImages(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
 
def extractMarkdownLink(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)",text)



def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception("No H1 title found in the markdown content")

def markdown_to_html_node(markdown_text):
    return markdown2.markdown(markdown_text)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file
    print(f"Reading markdown file from {from_path}")
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    print(f"Content from {from_path} read successfully.")
    print(f"Markdown content: \n{markdown_content}\n")

    # Extract the title
    print("Extracting title from markdown content.")
    title = extract_title(markdown_content)
    print(f"Extracted title: {title}")

    # Convert markdown to HTML
    print("Converting markdown to HTML.")
    html_content = markdown_to_html_node(markdown_content)
    print("Converted markdown to HTML successfully.")
    print(f"HTML content: \n{html_content}\n")

    # Verify and resolve the template file path
    abs_template_path = os.path.abspath(template_path)
    print(f"Absolute template path: {abs_template_path}")

    # Check if the template file exists and is readable
    if not os.path.isfile(abs_template_path):
        print(f"Template file {abs_template_path} does not exist.")
        return

    if not os.access(abs_template_path, os.R_OK):
        print(f"Template file {abs_template_path} is not readable.")
        return

    # Read the template file
    print(f"Reading template file from {template_path}")
    with open(abs_template_path, 'r') as template_file:
        template_content = template_file.read()
    print(f"Template content read successfully.")
    print(f"Template content: \n{template_content}\n")

    # Replace placeholders in template
    print("Replacing placeholders in the template.")
    final_content = template_content.replace("{{ Title }}", title)
    final_content = final_content.replace("{{ Content }}", html_content)
    print("Placeholders replaced successfully.")
    print(f"Final content: \n{final_content}\n")

    # Write the final content to the destination file
    print(f"Writing final HTML to {dest_path}")
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as output_file:
        output_file.write(final_content)
    print(f"Page generated successfully at {dest_path}")