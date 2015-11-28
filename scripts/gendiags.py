#!/bin/bash
#-!- encoding:utf8 -!-

import os, sys

# FUNCTIONS ---------------------------------------------------------------------------------------------------------------------------------------------
# This function prints usage of the script
def printUsage():
    print("Usage :\n\npython gendiags.py /path/to/plantuml.jar (png|[svg])\n");

# This function lists all the PUML files in rootDir
def getPUMLFiles(rootDir, excluded):
    PUMLFiles = [];
    for root, directories, filenames in os.walk(rootDir):
        for fname in filenames:
            if (".puml" in fname and not fname in excluded):
                PUMLFiles.append(root.replace(' ', '\ ').replace("'","\\'") + '/' + fname);
    return PUMLFiles;

# This function executes plantuml on target
def makePlantuml(plantumlJar, plantumlOptions, absolutePath):
    os.system("java -jar %s %s %s" % (plantumlJar, plantumlOptions, absolutePath));

# This function converts an svg to a png using inkscape
def inkscapeConvert(f):
    os.system("inkscape %s --export-eps=%s --export-ignore-filters --export-ps-level=3" % (f, f.replace('svg', 'eps')));
    
# This function moves src to dest
def move(src, dest):
    os.system("mv -f %s %s" % (src, dest));

# CONFIGURATION -----------------------------------------------------------------------------------------------------------------------------------------

EXCLUDED = ['skin.puml', 'variables.puml']

ROOT_DIR = os.path.dirname(os.path.realpath(__file__));
ROOT_DIR = ROOT_DIR[:-7];

SRC_DIR = ROOT_DIR + "diagram"

# ----------- PNG vars
DEST_DIR_PNG = ROOT_DIR + "report/figures/png/"
PUML_OPTIONS_PNG = "";

# ----------- SVG/EPS vars
DEST_DIR_SVG = ROOT_DIR + "report/figures/svg/"
DEST_DIR_EPS = ROOT_DIR + "report/figures/eps/"
PUML_OPTIONS_SVG = "-tsvg nbthread auto";

print("Running from %s" % ROOT_DIR);

TARGET = ""
if len(sys.argv) < 2:
    printUsage();
    exit();
elif len(sys.argv) == 3:
    TARGET = sys.argv[2];
    PLANTUML_PATH = sys.argv[1];
else:
    PLANTUML_PATH = sys.argv[1];

# SCRIPT --------------------------------------------------------------------------------------------------------------------------------------------

print("Starting production process...");
files = getPUMLFiles(SRC_DIR, EXCLUDED);
for f in files:
    if "png" in TARGET:
        print("Making PNG for %s" % f);
        makePlantuml(PLANTUML_PATH, PUML_OPTIONS_PNG, f);
        print("Moving PNG to %s" % DEST_DIR_PNG);
        move(f.replace("puml", "png"), DEST_DIR_PNG);
    else:
        print("Making SVG for %s" % f);
        makePlantuml(PLANTUML_PATH, PUML_OPTIONS_SVG, f);
        print("Converting SVG to EPS...");
        inkscapeConvert(f.replace("puml", "svg"))
        print("Moving SVG to %s" % DEST_DIR_SVG);
        move(f.replace("puml", "svg"), DEST_DIR_SVG);
        print("Moving EPS to %s" % DEST_DIR_EPS);
        move(f.replace("puml", "eps"), DEST_DIR_EPS);
