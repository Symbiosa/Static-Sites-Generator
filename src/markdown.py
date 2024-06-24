import markdown2
# def generatePage(fromPath, templatePath, destPath):
#     with open(fromPath, 'r') as file:
#         markdown_content = file.read()
        
#     title = extractTitle(markdown_content)
    
#     htmlNode = markdownToHtmlNode(markdown_content)
    
#     htmlContent = htmlNode.TO_HTML()
    
#     with open(templatePath, 'r') as file:
#         template_content = file.read()
        
#     finalContent = template_content.replace("{{ Title }}", title).replace("{{ Content }}", htmlContent)
    
#     destDir = os.path.dirname(destPath)
#     if not os.path.exists(destDir):
#         os.makedirs(destDir)
    
#     with open(destPath, 'w') as file:
#         file.write(finalContent)
    
    
#     print(f"Generating page from {fromPath} to {destPath} using {templatePath}")

def markdownToHtmlNode(markdownText):
    return markdown2.markdown(markdownText)

# example use:

def extractTitle(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            print(line.startswith('# '))
            return line[2:].strip()
    raise Exception("No H1 title found in the markdown content")