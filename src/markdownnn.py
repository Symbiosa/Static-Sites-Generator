import os
import markdown2  # Assuming markdown2 for markdown to HTML conversion, e.g., 'pip install markdown2'

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
    
    # Step 1: Read the markdown file
    print(f"Reading markdown file from {from_path}")
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    print(f"Content from {from_path} read successfully.")
    print(f"Markdown content: \n{markdown_content}\n")
    
    # Step 2: Extract the title
    print("Extracting title from markdown content.")
    title = extract_title(markdown_content)
    print(f"Extracted title: {title}")
    
    # Step 3: Convert markdown to HTML
    print("Converting markdown to HTML.")
    html_content = markdown_to_html_node(markdown_content)
    print("Converted markdown to HTML successfully.")
    print(f"HTML content: \n{html_content}\n")
    
    # Step 4: Verify template file exists and is readable
    abs_template_path = os.path.abspath(template_path)
    print(f"Absolute template path: {abs_template_path}")
    
    if not os.path.isfile(abs_template_path):
        print(f"Template file {abs_template_path} does not exist.")
        return
    
    if not os.access(abs_template_path, os.R_OK):
        print(f"Template file {abs_template_path} is not readable.")