from Bio import SeqIO

seq=""
for record in SeqIO.parse("assembly_01.fasta", "fasta"):
    if record.id == "contig_2":
        seq=str(record.seq)
seq=seq[10000:60000]
with open("blast.txt","w") as file:
    file.write(seq)
