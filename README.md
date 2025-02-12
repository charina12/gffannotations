# gff annotations
Convert .gff file to csv with annotations in columns

To use:
x is the path to your input file
out the path to your output file

Your input files should be a csv file with your gff annotation information. 
This can be created by using "Get Data" in Excel and selecting "From Text (Legacy)" then creating custom column headers. 
The annotation column you want stratified into columns MUST be named "annotations".
The annotation column data will look something like this:
ID=GFKNGCOL_00001;eC_number=4.1.1.98;Name=ubiD;db_xref=COG:COG0043;gene=ubiD;inference=ab initio prediction:Prodigal:002006,similar to AA sequence:UniProtKB:P0AAB4;locus_tag=GFKNGCOL_00001;product=3-octaprenyl-4-hydroxybenzoate carboxy-lyase

When you run this python script it will split the string at every ";" and put data into columns named with the information before the "=" and the values after the "=". For example:
              ID       eC_number  Name       db_xref   gene  ...      inference            locus_tag                             product
0  BMONBKAF_00001  1.14.13.24   mhbM  COG:COG0654  mhbM  ...  ab initio prediction:Prodigal:002006,similar to AA sequence:UniProtKB:Q5EXK1  BMONBKAF_00001  3-hydroxybenzoate 6-hydroxylase



