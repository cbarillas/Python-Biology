#/usr/bin/env python3
# Name: Carlos Barillas (cbarilla)
# Group Members: none

class Converter(str):

    def __new__(self, sequence):
        """Slices sequence & returns a string object w/o '@' symbol."""
        return str.__new__(self, sequence.upper())
    
    def translate(self):
        print(self+" = "+myDictionary.get(self,'Unknown'))

    """
    def translate(self):
        if self in DNACodonTable:
            self.translateDNACode()
        elif self in RNACodonTable:
            self.translateRNACode()
        elif self in aminoAcidTableOne or aminoAcidTableThree:
            self.translateAminoAcid()
        elif self not in DNACodonTable or RNACodonTable or aminoAcidTableOne:
            print('Unknown')

    def translateDNACode(self):
        #print(DNACodonTable[self])
        print(self+" = "+DNACodonTable.get(self,'Unknown'))

    def translateRNACode(self):
        print(self+" = "+RNACodonTable.get(self,'Unknown'))

    def translateAminoAcid(self):
        if len(self) == 1:
            print(self+" = "+aminoAcidTableOne.get(self,'Unknown'))
        elif len(self) == 3:
            print(self+" = "+aminoAcidTableThree.get(self,'Unknown'))

    def notFound(self):
        print('Unknown')
    
DNACodonTable = {
#                        Second Base
#        T             C             A             G
# T
    'TTT': 'PHE', 'TCT': 'SER', 'TAT': 'TYR', 'TGT': 'CYS',    # TxT
    'TTC': 'PHE', 'TCC': 'SER', 'TAC': 'TYR', 'TGC': 'CYS',    # TxC
    'TTA': 'LEU', 'TCA': 'SER', 'TAA': '---', 'TGA': '---',    # TxA
    'TTG': 'LEU', 'TCG': 'SER', 'TAG': '---', 'TGG': 'URP',    # TxG
# C
    'CTT': 'LEU', 'CCT': 'PRO', 'CAT': 'HIS', 'CGT': 'ARG',    # CxT
    'CTC': 'LEU', 'CCC': 'PRO', 'CAC': 'HIS', 'CGC': 'ARG',    # CxC
    'CTA': 'LEU', 'CCA': 'PRO', 'CAA': 'GLN', 'CGA': 'ARG',    # CxA
    'CTG': 'LEU', 'CCG': 'PRO', 'CAG': 'GLN', 'CGG': 'ARG',    # CxG
# A
    'ATT': 'ILE', 'ACT': 'THR', 'AAT': 'ASN', 'AGT': 'SER',    # AxT
    'ATC': 'ILE', 'ACC': 'THR', 'AAC': 'ASN', 'AGC': 'SER',    # AxC
    'ATA': 'ILE', 'ACA': 'THR', 'AAA': 'LYS', 'AGA': 'ARG',    # AxA
    'ATG': 'MET', 'ACG': 'THR', 'AAG': 'LYS', 'AGG': 'ARG',    # AxG
# G
    'GTT': 'VAL', 'GCT': 'ALA', 'GAT': 'ASP', 'GGT': 'GLY',    # GxT
    'GTC': 'VAL', 'GCC': 'ALA', 'GAC': 'ASP', 'GGC': 'GLY',    # GxC
    'GTA': 'VAL', 'GCA': 'ALA', 'GAA': 'GLU', 'GGA': 'GLY',    # GxA
    'GTG': 'VAL', 'GCG': 'ALA', 'GAG': 'GLU', 'GGG': 'GLY'     # GxG 
}

RNACodonTable = {
#                        Second Base
#        U             C             A             G
# U
    'UUU': 'PHE', 'UCU': 'SER', 'UAU': 'TYR', 'UGU': 'CYS',    # UxU
    'UUC': 'PHE', 'UCC': 'SER', 'UAC': 'TYR', 'UGC': 'CYS',    # UxC
    'UUA': 'LEU', 'UCA': 'SER', 'UAA': '---', 'UGA': '---',    # UxA
    'UUG': 'LEU', 'UCG': 'SER', 'UAG': '---', 'UGG': 'URP',    # UxG
# C
    'CUU': 'LEU', 'CCU': 'PRO', 'CAU': 'HIS', 'CGU': 'ARG',    # CxU
    'CUC': 'LEU', 'CCC': 'PRO', 'CAC': 'HIS', 'CGC': 'ARG',    # CxC
    'CUA': 'LEU', 'CCA': 'PRO', 'CAA': 'GLN', 'CGA': 'ARG',    # CxA
    'CUG': 'LEU', 'CCG': 'PRO', 'CAG': 'GLN', 'CGG': 'ARG',    # CxG
# A
    'AUU': 'ILE', 'ACU': 'THR', 'AAU': 'ASN', 'AGU': 'SER',    # AxU
    'AUC': 'ILE', 'ACC': 'THR', 'AAC': 'ASN', 'AGC': 'SER',    # AxC
    'AUA': 'ILE', 'ACA': 'THR', 'AAA': 'LYS', 'AGA': 'ARG',    # AxA
    'AUG': 'MET', 'ACG': 'THR', 'AAG': 'LYS', 'AGG': 'ARG',    # AxG
# G
    'GUU': 'VAL', 'GCU': 'ALA', 'GAU': 'ASP', 'GGU': 'GLY',    # GxU
    'GUC': 'VAL', 'GCC': 'ALA', 'GAC': 'ASP', 'GGC': 'GLY',    # GxC
    'GUA': 'VAL', 'GCA': 'ALA', 'GAA': 'GLU', 'GGA': 'GLY',    # GxA
    'GUG': 'VAL', 'GCG': 'ALA', 'GAG': 'GLU', 'GGG': 'GLY'     # GxG 
}

aminoAcidTableOne = {
    'A': 'ALA', 'R': 'ARG', 'N': 'ASN', 'D': 'ASP', 'B': 'ASX',
    'C': 'CYS', 'E': 'GLU', 'Q': 'GLN', 'Z': 'GLX', 'G': 'GLY',
    'H': 'HIS', 'I': 'ILE', 'L': 'LEU', 'K': 'LYS', 'M': 'MET',
    'F': 'PHE', 'P': 'PRO', 'S': 'SER', 'T': 'THR', 'W': 'TRP',
    'Y': 'TYR', 'V': 'VAL'
}

aminoAcidTableThree = {
    'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'ASX': 'B',
    'CYS': 'C', 'GLU': 'E', 'GLN': 'Q', 'GLX': 'Z', 'GLY': 'G',
    'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K', 'MET': 'M',
    'PHE': 'F', 'PRO': 'P', 'SER': 'S', 'THR': 'T', 'TRP': 'W',
    'TYR': 'Y', 'VAL': 'V'
}

"""
myDict = {               
#                      DNA Codon Table
#                        Second Base
#        T             C             A             G
# T
    'TTT': 'PHE', 'TCT': 'SER', 'TAT': 'TYR', 'TGT': 'CYS',    # TxT
    'TTC': 'PHE', 'TCC': 'SER', 'TAC': 'TYR', 'TGC': 'CYS',    # TxC
    'TTA': 'LEU', 'TCA': 'SER', 'TAA': '---', 'TGA': '---',    # TxA
    'TTG': 'LEU', 'TCG': 'SER', 'TAG': '---', 'TGG': 'URP',    # TxG
# C
    'CTT': 'LEU', 'CCT': 'PRO', 'CAT': 'HIS', 'CGT': 'ARG',    # CxT
    'CTC': 'LEU', 'CCC': 'PRO', 'CAC': 'HIS', 'CGC': 'ARG',    # CxC
    'CTA': 'LEU', 'CCA': 'PRO', 'CAA': 'GLN', 'CGA': 'ARG',    # CxA
    'CTG': 'LEU', 'CCG': 'PRO', 'CAG': 'GLN', 'CGG': 'ARG',    # CxG
# A
    'ATT': 'ILE', 'ACT': 'THR', 'AAT': 'ASN', 'AGT': 'SER',    # AxT
    'ATC': 'ILE', 'ACC': 'THR', 'AAC': 'ASN', 'AGC': 'SER',    # AxC
    'ATA': 'ILE', 'ACA': 'THR', 'AAA': 'LYS', 'AGA': 'ARG',    # AxA
    'ATG': 'MET', 'ACG': 'THR', 'AAG': 'LYS', 'AGG': 'ARG',    # AxG
# G
    'GTT': 'VAL', 'GCT': 'ALA', 'GAT': 'ASP', 'GGT': 'GLY',    # GxT
    'GTC': 'VAL', 'GCC': 'ALA', 'GAC': 'ASP', 'GGC': 'GLY',    # GxC
    'GTA': 'VAL', 'GCA': 'ALA', 'GAA': 'GLU', 'GGA': 'GLY',    # GxA
    'GTG': 'VAL', 'GCG': 'ALA', 'GAG': 'GLU', 'GGG': 'GLY',     # GxG 

#                       RNACodonTable 
#                        Second Base
#        U             C             A             G
# U
    'UUU': 'PHE', 'UCU': 'SER', 'UAU': 'TYR', 'UGU': 'CYS',    # UxU
    'UUC': 'PHE', 'UCC': 'SER', 'UAC': 'TYR', 'UGC': 'CYS',    # UxC
    'UUA': 'LEU', 'UCA': 'SER', 'UAA': '---', 'UGA': '---',    # UxA
    'UUG': 'LEU', 'UCG': 'SER', 'UAG': '---', 'UGG': 'URP',    # UxG
# C
    'CUU': 'LEU', 'CCU': 'PRO', 'CAU': 'HIS', 'CGU': 'ARG',    # CxU
    'CUC': 'LEU', 'CCC': 'PRO', 'CAC': 'HIS', 'CGC': 'ARG',    # CxC
    'CUA': 'LEU', 'CCA': 'PRO', 'CAA': 'GLN', 'CGA': 'ARG',    # CxA
    'CUG': 'LEU', 'CCG': 'PRO', 'CAG': 'GLN', 'CGG': 'ARG',    # CxG
# A
    'AUU': 'ILE', 'ACU': 'THR', 'AAU': 'ASN', 'AGU': 'SER',    # AxU
    'AUC': 'ILE', 'ACC': 'THR', 'AAC': 'ASN', 'AGC': 'SER',    # AxC
    'AUA': 'ILE', 'ACA': 'THR', 'AAA': 'LYS', 'AGA': 'ARG',    # AxA
    'AUG': 'MET', 'ACG': 'THR', 'AAG': 'LYS', 'AGG': 'ARG',    # AxG
# G
    'GUU': 'VAL', 'GCU': 'ALA', 'GAU': 'ASP', 'GGU': 'GLY',    # GxU
    'GUC': 'VAL', 'GCC': 'ALA', 'GAC': 'ASP', 'GGC': 'GLY',    # GxC
    'GUA': 'VAL', 'GCA': 'ALA', 'GAA': 'GLU', 'GGA': 'GLY',    # GxA
    'GUG': 'VAL', 'GCG': 'ALA', 'GAG': 'GLU', 'GGG': 'GLY',     # GxG 

#                   One Letter Amino Acid Table
 
    'A': 'ALA', 'R': 'ARG', 'N': 'ASN', 'D': 'ASP', 'B': 'ASX',
    'C': 'CYS', 'E': 'GLU', 'Q': 'GLN', 'Z': 'GLX', 'G': 'GLY',
    'H': 'HIS', 'I': 'ILE', 'L': 'LEU', 'K': 'LYS', 'M': 'MET',
    'F': 'PHE', 'P': 'PRO', 'S': 'SER', 'T': 'THR', 'W': 'TRP',
    'Y': 'TYR', 'V': 'VAL',


#                   Three Letter Amino Acid Table

    'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'ASX': 'B',
    'CYS': 'C', 'GLU': 'E', 'GLN': 'Q', 'GLX': 'Z', 'GLY': 'G',
    'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K', 'MET': 'M',
    'PHE': 'F', 'PRO': 'P', 'SER': 'S', 'THR': 'T', 'TRP': 'W',
    'TYR': 'Y', 'VAL': 'V'
}

seq = input("Enter either an amino acid code or a codon code to convert : ")
code = Converter(seq)
code.translate()
