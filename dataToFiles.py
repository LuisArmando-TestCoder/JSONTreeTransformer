import json
import os

functionInsight =  "{\n"
functionInsight += "  presetScene({\n"
functionInsight += "    setup({ renderer, scene, camera, defaultScene }) {\n"
functionInsight += "    },\n"
functionInsight += "    animate({ renderer, scene, camera, defaultScene }) {\n"
functionInsight += "    },\n"
functionInsight += "  })\n"
functionInsight += "}"

def createFolder(folderPath):
    accessRights = 0o755

    try:
        os.mkdir(folderPath, accessRights)
    except OSError:
        print ("Creation of the directory %s failed" % folderPath)
    else:
        print ("Successfully created the directory %s" % folderPath)

def createThreeJSFile(item, folderPath):
    file = open("../../src/scenes/" + folderPath + "/" + item["name"] + ".ts","w+")

    file.write("import * as THREE from 'three'\r\n")
    file.write("import presetScene from '../../scenePreset'\r\n")
    file.write("// " + item["link"] + "\r\n")
    file.write("export default function " + item["name"] + r"() ")
    file.write(functionInsight)
    file.close()

def transformDataToThreeJSFiles(fileNames, fileJson):
    for fileName in fileNames:
        folderPath = "../../src/scenes/" + fileName

        createFolder(folderPath)
        
        for _, item in enumerate(fileJson[fileName]):
            createThreeJSFile(item, folderPath)

def getThreeJSFileNames(fileJson):
    fileNames = []

    for attr in fileJson:
        fileNames.append(attr)
    
    return fileNames


fileContent = open("threeJSImports.json").read()
fileJson = json.loads(fileContent)
fileNames = getThreeJSFileNames(fileJson)

transformDataToThreeJSFiles(fileNames, fileJson)
