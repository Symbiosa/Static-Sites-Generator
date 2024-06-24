import markdown2
import os
def markdownToHtmlNode(markdownText):
    return markdown2.markdown(markdownText)

# example use:

def extractTitle(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception("No H1 title found in the markdown content")

# def generatePage(fromPath, templatePath, destPath):
#     print(f"Generating page from {fromPath} to {destPath} using {templatePath}")
    
#     # Step 1: Read the markdown file
#     print(f"Reading markdown file from {fromPath}")
#     with open(fromPath, 'r') as file:
#         markdown_content = file.read()
#     print(f"Content from {fromPath} read successfully.")
#     print(f"Markdown content: \n{markdown_content}\n")
    
#     # Step 2: Extract the title
#     print("Extracting title from markdown content.")
#     title = extractTitle(markdown_content)
#     print(f"Extracted title: {title}")
    
#     # Step 3: Convert markdown to HTML
#     print("Converting markdown to HTML.")
#     htmlContent = markdownToHtmlNode(markdown_content)
#     print("Converted markdown to HTML successfully.")
#     print(f"HTML content: \n{htmlContent}\n")
    
#     # Step 4: Verify template file exists and is readable
#     if not os.path.isfile(templatePath):
#         print(f"Template file {templatePath} does not exist.")
#         return
    
#     print(f"Template file {templatePath} exists and is accessible.")
#     with open(templatePath, 'r') as file:
#         template_content = file.read()
    
#     if not template_content:
#         print(f"Template file {templatePath} is empty.")
#         return
    
#     print(f"Template from {templatePath} read successfully.")
#     print(f"Template content: \n{template_content}\n")
    
#     # Step 5: Replace the placeholders in the template
#     print("Replacing placeholders in the template.")
#     finalContent = template_content.replace("{{ Title }}", title).replace("{{ Content }}", htmlContent)
#     print("Replaced placeholders in the template successfully.")
#     print(f"Final content: \n{finalContent}\n")
    
#     # Step 6: Create directories if needed and write the new HTML to the destination file
#     destDir = os.path.dirname(destPath)
#     print(f"Ensuring directory {destDir} exists.")
#     if not os.path.exists(destDir):
#         os.makedirs(destDir)
#         print(f"Created directory {destDir}.")
    
#     print(f"Writing final content to {destPath}")
#     with open(destPath, 'w') as file:
#         file.write(finalContent)
#         print(f"Final content written to {destPath} successfully.")
    