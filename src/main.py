from textnode import (
    TextNode,
    textTypeText,
    textTypeBold,
    textTypeItalic,
    textTypeCode
)

from markdown_blocks import (
    markdownToBlocks,
    blockToBlockType,
    blockTypeCode,
    blockTypeHeading,
    blockTypeListOrdered,
    blockTypeListUnordered,
    blockTypeParagraph,
    blockTypeQuote,
)
#from markdownn import extractTitle, generatePage, markdownToHtmlNode
from markdown import generate_page, splitNodesImage, splitNodesLink, splitNodesDelimiter, textToTextnodes
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

def generatePageRecur(fromDir, templatePath, destDir):
    print(f"Generating page for every markdown file in {fromDir} to {destDir} using {templatePath}")
    if not os.path.exists(destDir):
        print(f"{destDir} doesn't exist")
        raise TypeError(f"{destDir} gone MIA, call the Boots")
    
    for item in os.listdir(fromDir):
        srcPath = os.path.join(fromDir, item)
        destPath = os.path.join(destDir, item.replace('.md', '.html'))
        
        if os.path.isfile(srcPath):
            print(f"{srcPath} is a file")
            
            if srcPath.endswith('.md'):
                generate_page(srcPath,templatePath,destPath)
                print(f'Succesfully converted {srcPath}')
        
        elif os.path.isdir(srcPath):
            print(f"{srcPath} is a dir, diving deeper")
            newDestDir = os.path.join(destDir, item)
            
            if not os.path.exists(newDestDir):
                os.makedirs(newDestDir)
            
            generatePageRecur(srcPath, templatePath, newDestDir)
        
def main():
    fromDir = "content"               #path to from dir
    templatePath = "template.html"     #path to template being used
    destDir = "public"                #path to destination dir
    print(fromDir)
    print(templatePath)
    print(destDir)
    generate_page(fromDir,templatePath,destDir)
main()