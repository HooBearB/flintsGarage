import os

def initFile():
    content = []
    content.append("<!DOCTYPE html>\n")
    content.append("<html>\n")
    content.append("  	<head>\n")
    content.append("		<meta charset=\"UTF-8\">\n")
    content.append("		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
    content.append("		<title>Flint's Garage - Roadmap</title>\n")
    content.append("		<link rel=\"icon\" href=\"images/icon.png\">\n")
    content.append("  	</head>\n")
    content.append("\n")
    content.append("  	<body>\n")
    return content

def runFile(content, directory = os.path.dirname(__file__)):
    content.append("    <h1>Index of flintsgarage.neocities.org" + directory[15:] + "/</h1>\n")
    content.append("    <hr>\n")
    if directory != os.path.dirname(__file__):
        parent = os.path.abspath(os.path.join(directory, os.pardir))
        if parent == os.path.dirname(__file__):
            parent = parent[16:] + "roadmap.html"
        else:
            parent = parent[16:] + "/roadmap.html"
        content.append("        <a href=\"flintsgarage.neocities.org/" + parent + "/\"><p>Go back up a directory</p></a>\n")
        content.append("        <br>\n")
    dirlist = os.listdir(directory)
    walk = 0
    directories = []
    while walk < len(dirlist):
        item = dirlist[walk]
        if not os.path.isfile(directory + "\\" + item) and item not in [".git"]:
            print(item + " is a folder")
            directories.append(directory + "\\" + item)
            content.append("        <a href=\"https://flintsgarage.neocities.org/" + item + "/roadmap.html\"><p><img src=\"https://raw.githubusercontent.com/redbooth/free-file-icons/master/48px/_blank.png\" style=\"position:relative; bottom:-10px;\" height=\"24px\" width=\"24px\">" + item + "</p>\n")
        walk = walk + 1
    walk = 0
    while walk < len(dirlist):
        item = dirlist[walk]
        dirlen = 0
        if os.path.isfile(directory + "\\" + item) and item != "roadmap.html":
            type = item[-4:]
            if directory != os.path.dirname(__file__):
                item = directory[16:] + "\\" + item
                dirlen = len(directory[15:])
            print(item + " is a file")
            if type == ".png":
                content.append("        <a href=\"/" + item + "\"><p><img src=\"https://raw.githubusercontent.com/redbooth/free-file-icons/master/48px/png.png\" style=\"position:relative; bottom:-10px;\" height=\"24px\" width=\"24px\">" + item[dirlen:] + "</p></a>\n")
            if type == "html":
                content.append("        <a href=\"/" + item + "\"><p><img src=\"https://raw.githubusercontent.com/redbooth/free-file-icons/master/48px/html.png\" style=\"position:relative; bottom:-10px;\" height=\"24px\" width=\"24px\">" + item[dirlen:] + "</p></a>\n")
            if type in [".jpg", "jpeg"]:
                content.append("        <a href=\"/" + item + "\"><p><img src=\"https://raw.githubusercontent.com/redbooth/free-file-icons/master/48px/jpeg.png\" style=\"position:relative; bottom:-10px;\" height=\"24px\" width=\"24px\">" + item[dirlen:] + "</p></a>\n")
            if type == ".css":
                content.append("        <a href=\"/" + item + "\"><p><img src=\"https://raw.githubusercontent.com/redbooth/free-file-icons/master/48px/css.png\" style=\"position:relative; bottom:-10px;\" height=\"24px\" width=\"24px\">" + item[dirlen:] + "</p></a>\n")
            if type == ".txt":
                content.append("        <a href=\"/" + item + "\"><p><img src=\"https://raw.githubusercontent.com/redbooth/free-file-icons/master/48px/txt.png\" style=\"position:relative; bottom:-10px;\" height=\"24px\" width=\"24px\">" + item[dirlen:] + "</p></a>\n")
            if type == ".pdf":
                content.append("        <a href=\"/" + item + "\"><p><img src=\"https://raw.githubusercontent.com/redbooth/free-file-icons/master/48px/pdf.png\" style=\"position:relative; bottom:-10px;\" height=\"24px\" width=\"24px\">" + item[dirlen:] + "</p></a>\n")
            if type in [".ttf", "woff", "off2"]:
                content.append("        <a href=\"/" + item + "\"><p><img src=\"https://raw.githubusercontent.com/redbooth/free-file-icons/master/48px/_blank.png\" style=\"position:relative; bottom:-10px;\" height=\"24px\" width=\"24px\">" + item[dirlen:] + "</p></a>\n")
        walk = walk + 1
    content.append("        <p>All icons on this page are retrieved directly from <a href=\"https://github.com/redbooth/free-file-icons\">https://github.com/redbooth/free-file-icons</a> which is licensed under the MIT License.</p>\n")
    content.append("  	</body>\n")
    content.append("</html>\n")
    return content, directories

def saveFile(content, directory = os.path.dirname(__file__)):
    savefile = open(directory + "/roadmap.html", "w")
    walk = 0
    while walk < len(content):
        content[walk] = content[walk].replace("\\", "/")
        walk = walk + 1
    savefile.writelines(content)

def rootFolders(directories):
    walk = 0
    while walk < len(directories):
        print(directories[walk])
        file = initFile()
        file, folders = runFile(file, directories[walk])
        saveFile(file, directories[walk])
        rootFolders(folders)
        walk = walk + 1

file = initFile()
file, folders = runFile(file)
saveFile(file)
rootFolders(folders)