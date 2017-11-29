#!/usr/bin/env python

import argparse
import re

def get_arguments():

    parser = argparse.ArgumentParser(description="Generates Eigenstrat .snp and .ind files \
                                                  for use with AdmixTools software package")
    
    parser.add_argument("-f", "--infile", type=str, required=True, help="Input filename in phylip format")
    parser.add_argument("-i", "--ind", type=str, required=False, help="ind output filename; Default = out.ind", 
                        nargs="?", default="out.ind")    
    parser.add_argument("-s", "--snp", type=str, required=False, help="snp output filename; Default = out.snp", 
                        nargs="?", default="out.snp")                        
    args = parser.parse_args()
    
    return args
    
    
def read_infile(infile):

    columns = []
    sampleIDs = []
    
    phylip = re.compile(r"^(\d+)\s+(\d+)\s*$")
    
    with open(infile) as fin:
        for line in fin:
            m = phylip.search(line)
            if m:
                header = line.strip()
            else:
                columns.append([x for x in line.strip().split()])
        
        for col in columns:
            sampleIDs.append(col[0])
    
    return header, sampleIDs
    
    
def make_outfiles(list, indfile, snpfile, header):

    with open(indfile, "w") as out:
        for line in list:
            make_indfile(line, out)
  
    with open(snpfile, "w") as out:
        make_snpfile(line, out, header)
            

def make_indfile(line, file):

    file.write(line + "\t" + "U" + "\t" + "Pop" + "\n")
    
def make_snpfile(line, file, header):
    
    initial = 0.000000
    numInd, loci = header.split()
    for i in range(0, int(loci)):
        file.write("a" + "_" + str(i) + "\t" + "1" + "\t" + '%0.6f' % initial + "\t" + str(i) + "\n")
        initial += 0.000010
        
    
#####################################################################################################    
##################################MAIN###############################################################
#####################################################################################################


args = get_arguments()

IDs = []
header, IDs = read_infile(args.infile)

make_outfiles(IDs, args.ind, args.snp, header)