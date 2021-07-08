from Bio.Align.Applications import MuscleCommandline
from io import StringIO
from Bio import AlignIO
import sys

f=open("leer.txt","w")
muscle_program=r'muscle3.8.31_i86win32.exe'
entrada=sys.argv[1]

muscle_cline = MuscleCommandline(muscle_program,input = entrada)
stdout, stderr = muscle_cline()

align = AlignIO.read(StringIO(stdout), "fasta")


print(align)

f.write("------- RESULTADO DEL ALINEAMIENTO ---------\n")

for i in (align):
  f.write(str(i)+'\n')

f.write("----------------------------------\n")
f.close()