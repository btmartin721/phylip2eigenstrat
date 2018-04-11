**Script to generate Eigenstrat input files used in AdmixTools (and other) software packages: .snp and .ind  
The script was intended for RAD or ddRAD data, which do not usually have cM or physical distance information.**

______________________________________________________________________________________________________________________

Usage: `phylip2eigenstrat.py -f [--infile] *.phylip -i [--ind <ind outfile>] *.ind -s [--snp <snp outfile>] *.snp`


The only required command-line flag is -f. If -i and -s are not specified, default = out.ind, out.snp  

This script requires a phylip file as input to obtain the sample names and number of loci  
The Phylip file should be from the same run as the .geno file to ensure the same number of loci  

After running this script, you will need to go into the .ind file and change each "Pop" to a population code  
The population identifier should be a unique string for each population.  

AdmixTools and Eigensoft require a third input file that is produced in pyRAD: .geno  
Please note that AdmixTools requires the three input files to have .geno, .snp, and .ind extensions.  


## Citations

Example PHYLIP and .geno datasets were downloaded from the Dryad repository. The citations are listed below:

> Prates I, Xue AT, Brown JL, Alvarado-Serrano DF, Rodrigues MT, Hickerson MJ, Carnaval AC. (2016). Inferring responses to climate > dynamics from historical demography in neotropical forest lizards. Proceedings of the National Academy of Sciences of the United > States of America 113(129): 7978–7985. https://doi.org/10.1073/pnas.1601063113

Dryad data package:

> Prates I, Xue AT, Brown JL, Alvarado-Serrano DF, Rodrigues MT, Hickerson MJ, Carnaval AC. (2016). 
> Data from: Inferring responses to climate dynamics from historical demography in neotropical forest lizards. 
> Dryad Digital Repository. https://doi.org/10.5061/dryad.2v1p6
