#!/bin/bash
#-!- encoding:utf8 -!-

import os, sys

# FUNCTIONS ---------------------------------------------------------------------------------------------------------------------------------------------------------
def printUsage():
    print("Usage :\n\npython gendiagsSVG.py /path/to/plantuml.jar\n");

def getPUMLFiles(rootDir, excluded):
    PUMLFiles = [];
    for root, directories, filenames in os.walk(rootDir):
        for fname in filenames:
            if (".puml" in fname and not fname in excluded):
                PUMLFiles.append(root.replace(' ', '\ ').replace("'","\\'") + '/' + fname);
    return PUMLFiles;

def makePNG(plantumlJar, plantumlOptions, absolutePath):
    os.system("java -jar %s %s %s" % (plantumlJar, plantumlOptions, absolutePath));

def moveSVG(src, dest):
    os.system("mv -f %s %s" % (src, dest));

# CONFIGURATION -----------------------------------------------------------------------------------------------------------------------------------------------------

EXCLUDED = ['skin.puml', 'variables.puml']

ROOT_DIR = os.path.dirname(os.path.realpath(__file__));
print(ROOT_DIR)
ROOT_DIR = ROOT_DIR[:-7] + "diagram";
DEST_DIR = ROOT_DIR[:-7] + "report/figures/svg/"
DEST_DIR_EPS = ROOT_DIR[:-7] + "report/figures/eps/"

print("Root dir is %s" % ROOT_DIR);
print("Destination dir is %s" % DEST_DIR);

PLANTUML_OPTIONS = "-tsvg nbthread auto";

if len(sys.argv) < 2:
    printUsage();
    exit();
else:
    PLANTUML_PATH = sys.argv[1];

# SCRIPT ------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Starting production process...");
files = getPUMLFiles(ROOT_DIR, EXCLUDED);
for f in files:
    print("Making SVG for %s" % f);
    makePNG(PLANTUML_PATH, PLANTUML_OPTIONS, f);
    print("Moving SVG to report/figures/SVG");
    moveSVG(f.replace("puml", "svg"), DEST_DIR);
