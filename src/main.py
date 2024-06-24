from textnode import TextNode
from markdownn import extractTitle, generatePage, markdownToHtmlNode
from markdownnn import generate_page
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
    #srcDir = "./static"
    #destDir = "./public"
    #if os.path.exists(destDir):
        #print(f"removing old {destDir} and recreating it")
        #shutil.rmtree(destDir)
        #os.makedirs(destDir)
    #recur(srcDir,destDir)
    # fromPath = "./content/index.md"
    # templatePath = "/home/lab/workspace/github.com/SYMBIOSA/StaticSites/template.html"
    # destPath = "./public/index.html"
    # generatePage(fromPath,templatePath,destPath)
    from_path = "./content/index.md"
    template_path = "./template.html"
    dest_path = "./public/index.html"
    generate_page(from_path, template_path,dest_path)
main()