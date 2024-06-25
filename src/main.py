from textnode import TextNode
#from markdownn import extractTitle, generatePage, markdownToHtmlNode
from markdown import generate_page, splitNodesImage, splitNodesDelimiter
import os
import shutil

def recur(src, dest):
    if not os.path.exists(dest):
        print(f"{dest} doesnt exist, fixing it")
        os.mkdir(dest)
    
    for item in os.listdir(src):
        srcPath = os.path.join(src,item)
        destPath = os.path.join(dest,item)

        if os.path.isfile(srcPath):
            print(f"{srcPath} has been copied")
            shutil.copy(srcPath,destPath)
        elif os.path.isdir(srcPath):
            if not os.path.exists(destPath):
                os.mkdir(destPath)
                print(f"{destPath} new directory created to destination")
            print("diving deeper")
            recur(srcPath,destPath)
    
def main():
    # from_path = "./content/index.md"
    # template_path = "./template.html"
    # dest_path = "./public/index.html"
    # generate_page(from_path, template_path,dest_path)
    node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    "text_type_text",
    )
    splitNodesImage(node)
    print(splitNodesImage)
    
main()