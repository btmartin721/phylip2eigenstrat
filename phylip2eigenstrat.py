#!/usr/bin/env python

import argparse
import re

from datastruct import Struct

def get_arguments():

    parser = argparse.ArgumentParser(description="Generates Eigenstrat .snp and .ind files \
                                                  for use with AdmixTools software package")
    parser.add_argument("-p", "--phylip", type=str, required=True, help="Input filename in PHYLIP format")
    parser.add_argument("-i", "--ind", type=str, required=False, help="ind output filename; Default = out.ind", 
                        nargs="?", default="out.ind")    
    parser.add_argument("-n", "--snp", type=str, required=False, help="snp output filename; Default = out.snp", 
                        nargs="?", default="out.snp")    
    parser.add_argument("-s", "--start", type=int, required=False, nargs="?", default="1",
                        help="Specify first character of sample ID to be used as pattern for population ID; default=1")
    parser.add_argument("-e", "--end", type=int, required=False, nargs="?", default="4",
                        help="Specify last character of sample ID to be used as pattern for population ID; default=4")
                        
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
    
def read_phylip(line):

    line = line.rstrip("\r\n")
    ids_loci = line.strip().split(None, 1)
    ids = ids_loci[0]
    loc = ids_loci[1]

    return ids, loc, header
    
    
def make_outfiles(Ids, indfile, snpfile, header, pattern, loci):

    make_indfile(Ids, indfile, pattern)
    make_snpfile(snpfile, header)
            

def make_indfile(ID, file, pattern):

    file.write(ID + "\t" + "U" + "\t" + pattern + "\n")
    
def make_snpfile(file, header):
    
    initial = 0.000000
    numInd, loci = header.split()
    for i in range(1, int(loci)+1):
        file.write("a" + "_" + str(i) + "\t" + "1" + "\t" + '%0.6f' % initial + "\t" + str(i) + "\n")
        initial += 0.000010
        
def get_unique_identifiers(pattern, hit, number):

    if not hit:
        dataset.make_dict(number, hit, pattern)

    elif pattern not in hit:
        number += 1
        dataset.make_dict(number, hit, pattern)

    return number
        
    
#####################################################################################################    
##################################MAIN###############################################################
#####################################################################################################


args = get_arguments()

unique_ids = dict()
IDs = list()

popnum = 1

with open(args.phylip, "r") as fin:
    with open(args.ind, "w") as indout:
        with open(args.snp, "w") as snpout:

            header = fin.readline()
            header = header.rstrip()

            for lines in fin:
                ids, loc, header = read_phylip(lines)

                dataset = Struct(ids, loc)
                
                patt = dataset.id[args.start-1:args.end]
                popnum = get_unique_identifiers(patt, unique_ids, popnum)  # Returns popID and adds 1 for each unique ID
                popid = unique_ids[patt]   # dictionary with unique ids (key), popID (value)
                
                make_indfile(dataset.id, indout, str(patt))
                
            make_snpfile(snpout, header)