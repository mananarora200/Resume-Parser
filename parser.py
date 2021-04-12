# download en_core_web_sm
# python -m spacy download en_core_web_sm
# python -m nltk.downloader words
# python -m nltk.downloader stopwords

from pyresparser import ResumeParser
# github: https://github.com/OmkarPathak/pyresparser
import json
import os

def getResume(filePath):
    for path in os.listdir(filePath):
        parseDocument(filePath+'/'+path)

def parseDocument(filePath):
    parse = ResumeParser(filePath)
    data = parse.get_extracted_data()
    fileObject = open(f"output/{data['name']}.json","w")
    json.dump(data,fileObject)

if __name__ == "__main__":
    filePath = "samples"
    getResume(filePath)
    print("Done")

