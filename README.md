**Script to generate Eigenstrat input files used in AdmixTools (and other) software packages: .snp and .ind  
The script was intended for RAD or ddRAD data, which do not usually have cM or physical distance information.**

______________________________________________________________________________________________________________________

Usage:

```
phylip2eigenstrat.py -p [--phylip] *.phy -i [--ind <ind outfile>] *.ind -s [--snp <snp outfile>] *.snp [options]...
```

Mandatory arguments:

[-p, --phylip - Input PHYLIP file from the same pyRAD run as the .geno file]  

Optional arguments:  

[-i, --ind - Specifies .ind output file; default = out.ind]  
[-n, --snp - Specifies .snp output file; default = out.snp]  
[-s, --start - Starting character for popID search pattern; default = 1]  
[-e, --end - Last character for popID search pattern; default = 4]  


The only required command-line flag is -p. If -i and -n are not specified, default = out.ind, out.snp    

This script requires a phylip file as input to obtain the sample names and number of loci  
The Phylip file should be from the same pyRAD run as the .geno file to ensure the same number of loci  

The Phylip file also uses a REGEX pattern to determine population IDs in the .ind file  
The characters used for the REGEX can be changed with the -s and -e options (default = 1-4)    


AdmixTools and Eigensoft require a third input file that is produced in pyRAD: .geno  
Please note that AdmixTools requires the three input files to have .geno, .snp, and .ind extensions.  


## Citations  

Example PHYLIP and .geno datasets were downloaded from the Dryad repository. The citations are listed below:

> Prates I, Xue AT, Brown JL, Alvarado-Serrano DF, Rodrigues MT, Hickerson MJ, Carnaval AC. (2016). Inferring responses to climate > dynamics from historical demography in neotropical forest lizards. Proceedings of the National Academy of Sciences of the United > States of America 113(129): 7978–7985. https://doi.org/10.1073/pnas.1601063113

Dryad data package:

> Prates I, Xue AT, Brown JL, Alvarado-Serrano DF, Rodrigues MT, Hickerson MJ, Carnaval AC. (2016). Data from: Inferring responses to climate dynamics from historical demography in neotropical forest lizards. Dryad Digital Repository. https://doi.org/10.5061/dryad.2v1p6
