from textnode import TextNode
from markdown import extractTitle, markdownToHtmlNode
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

def generatePage(fromPath, templatePath, destPath):
    with open(fromPath, 'r') as file:
        markdown_content = file.read()
        print("We read FromPath")
        
    title = extractTitle(markdown_content)
    
    htmlContent = markdownToHtmlNode(markdown_content)
    print(os.path.dirname(templatePath))
    with open(templatePath, 'r') as file:
        template_content = file.read()
        print("Lets read template")
    print(template_content)
    finalContent = template_content.replace("{{ Title }}", title).replace("{{ Content }}", htmlContent)
    print(finalContent)
    destDir = os.path.dirname(destPath)
    if not os.path.exists(destDir):
        os.makedirs(destDir)
        print("path was not found")
    
    with open(destPath, 'w') as file:
        file.write(finalContent)
        print("Intense typing")
    
    
    print(f"Generating page from {fromPath} to {destPath} using {templatePath}")

def main():
    #srcDir = "./static"
    #destDir = "./public"
    #if os.path.exists(destDir):
        #print(f"removing old {destDir} and recreating it")
        #shutil.rmtree(destDir)
        #os.makedirs(destDir)
    #recur(srcDir,destDir)
    fromPath = "./content/index.md"
    templatePath = "./template.html"
    destPath = "./public/index.html"
    generatePage(fromPath,templatePath,destPath)
main()