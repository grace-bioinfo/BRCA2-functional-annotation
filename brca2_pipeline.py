import requests 
import time
from Bio.Seq import Seq
from Bio import Entrez, SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
Entrez.email = "gracekagendonyaga@gmail.com"




# brca2_seq = SeqIO.read("BRCA2_homo_sapiens.fasta", "fasta")

# blast_process = NCBIWWW.qblast(
#     program = "blastp",
#     database = "nr",
#     sequence = brca2_seq.seq
# )

# with open ("blast_result.xml", "w") as b:
#     b.write(blast_process.read())

# print("BRCA2 blast was a success!")

# ids = []

# with open("blast_result.xml") as b:
#     blast_records = NCBIXML.parse(b)

#     count = 0
#     with open("filtered_results.txt", "w") as b:
#          for blast_record in blast_records:
#              for alignment in blast_record.alignments:
#                  print(alignment.title, file=b)
#                  for hsp in alignment.hsps:
#                      identity_percent = (hsp.identities / hsp.align_length)*100
#                      if hsp.expect < 0.05 and identity_percent > 98:
#                          ids.append(alignment.accession)
#                          count += 1
#                          print("Score:", hsp.score, file=b)
#                          print("E-value:", hsp.expect, file=b)
#                          print("Identity:", hsp.identities, file=b)
#                          print("Identity %:", round(identity_percent, 5), file=b)
#                          print("Gaps:", hsp.gaps, file=b)
#                          # print("Query Sequence:", hsp.query)
#                          # print("Match Sequence:", hsp.sbjct)
#                          print("-"*50, file=b)
#                          print("Accessions collected:", len(ids))              
#                          print("Total Significant Hits:", count, file=b)

# send our 28 ids(accession numbers) to NCBI to get sequences. Here we use Entrez.
# Entrez helps you to search NCBI databases, fetch the records and use the sequences.
# Above, we would have written only 2 lines of code(line 42,43) to get the sequences from the 
# blast result file, it also applies, but i opted to use a longer method for practice

# fetch_homologs = Entrez.efetch(
#     db = "protein",
#     id = ids,
#     rettype = "fasta",
#     retmode = "text"
# )  
# # # create a readable file to store the information

# with open("homologs.fasta", "w")as homologs:
#     homologs.write(fetch_homologs.read())

#     print("Homolog fetching was a success yay!")

# Alignment is the next step. A free tool has already been provided by 
# The EMBL-EBI Job Dispatcher sequence analysis tools framework in 2024. it helps in 
# especially, to chech for mutations, it can create phylogenetic trees among many other functions.
# I love that it exists.


 








               

