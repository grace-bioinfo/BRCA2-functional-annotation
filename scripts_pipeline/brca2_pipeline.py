from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML



# brca2_seq = SeqIO.read("BRCA2_homo_sapiens.fasta", "fasta")

# blast_process = NCBIWWW.qblast(
#     program = "blastp",
#     database = "nr",
#     sequence = brca2_seq.seq
# )

# with open ("blast_result.xml", "w") as b:
#     b.write(blast_process.read())

# print("BRCA2 blast was a success!")

with open("blast_result.xml") as b:
    blast_records = NCBIXML.parse(b)

    count = 0
    with open("filtered_results.txt", "w") as b:
         for blast_record in blast_records:
             for alignment in blast_record.alignments:
                 print(alignment.title, file=b)
                 for hsp in alignment.hsps:
                     identity_percent = (hsp.identities / hsp.align_length)*100
                     if hsp.expect < 0.05 and identity_percent > 98:
                         count += 1
                         print("Score:", hsp.score, file=b)
                         print("E-value:", hsp.expect, file=b)
                         print("Identity:", hsp.identities, file=b)
                         print("Identity %:", round(identity_percent, 5), file=b)
                         print("Gaps:", hsp.gaps, file=b)
                         # print("Query Sequence:", hsp.query)
                         # print("Match Sequence:", hsp.sbjct)
                         print("-"*50, file=b)
                        
         print("Total Significant Hits:", count, file=b)

               

