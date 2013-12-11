#!/bin/python
#
#title           :Filter fasta
#description     :Filters fasta file given a list of IDs
#author          :Stephan Pabinger
#

def readGeneNames(filename):
  genes = list()
  with open(filename, "r") as f:
    for line in f:
      genes.append(line.strip())
      #print line
  
  return genes
      
def filterFasta(filename, output, genes):
  with open(filename, "r") as f:
    with open(output, "w") as output:
      
      toPrint = 0    #flag to enable printing of sequence
      juhuCount = 0
      
      for line in f:
        line = line.strip()
        # check if new sequence starts (with ">")
        if (line.startswith(">")):
          strippedLine = line.strip(">")
          #check if id is in geneNames list -> enable printing
          if (strippedLine in genes):
            toPrint = 1
          else:
            toPrint = 0  #prining should be stopped here
            
        if (toPrint):
          output.write(line + "\n")
      

# 
# end filterFasta
      
      
      
print "Starting filtering fasta file ..."
genes = readGeneNames("geneNames.txt")
#print genes
filterFasta("jatropha.fasta", "jatrophaFiltered.fasta", genes)

print "... done."


