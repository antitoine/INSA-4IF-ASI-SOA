#!/bin/bash
#-!- encoding:utf8 -!-

import os, sys

# FUNCTIONS ---------------------------------------------------------------------------------------------------------------------------------------------------------
def printUsage():
    print("Usage :\n\npython gendiags.py /path/to/plantuml.jar\n");

def getPUMLFiles(rootDir, excluded):
    PUMLFiles = [];
    for root, directories, filenames in os.walk(rootDir):
        for fname in filenames:
            if (".puml" in fname and not fname in excluded):
                PUMLFiles.append(root.replace(' ', '\ ') + '/' + fname);
    return PUMLFiles;

def makePNG(plantumlJar, plantumlOptions, absolutePath):
    os.system("java -jar %s %s %s" % (plantumlJar, plantumlOptions, absolutePath));

# CONFIGURATION -----------------------------------------------------------------------------------------------------------------------------------------------------

EXCLUDED = ['skin.puml']

ROOT_DIR = os.path.dirname(os.path.realpath(__file__));
print(ROOT_DIR)
ROOT_DIR = ROOT_DIR[:-7] + "diagram";
print("Root dir is %s" % ROOT_DIR);

PLANTUML_OPTIONS = "";

if len(sys.argv) < 2:
    printUsage();
    exit();
else:
    PLANTUML_PATH = sys.argv[1];

# SCRIPT ------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Starting production process...");
files = getPUMLFiles(ROOT_DIR, EXCLUDED);
for f in files:
    print("Making PNG for %s" % f);
    makePNG(PLANTUML_PATH, PLANTUML_OPTIONS, f);
