#!/usr/bin/env python3
# Carlos Barillas
# None


class ProteinParam(str):
    # These tables are for calculating:
    #     molecular weight (aa2mw), along with the mol. weight of H2O (mwH2O)
    #     absorbance at 280 nm (aa2abs280)
    #     pKa of positively charged Amino Acids (aa2chargePos)
    #     pKa of negatively charged Amino acids (aa2chargeNeg)
    #     and the constants aaNterm and aaCterm for pKa of the respective termini
    #  Feel free to move these to appropriate methods as you like

    # As written, these are accessed as class attributes, for example:
    # ProteinParam.aa2mw['A'] or ProteinParam.mwH2O

    aa2mw = {
        'A': 89.093, 'G': 75.067, 'M': 149.211, 'S': 105.093, 'C': 121.158,
        'H': 155.155, 'N': 132.118, 'T': 119.119, 'D': 133.103, 'I': 131.173,
        'P': 115.131, 'V': 117.146, 'E': 147.129, 'K': 146.188, 'Q': 146.145,
        'W': 204.225, 'F': 165.189, 'L': 131.173, 'R': 174.201, 'Y': 181.189
    }

    mwH2O = 18.015
    aa2abs280 = {'Y': 1490, 'W': 5500, 'C': 125}

    aa2chargePos = {'K': 10.5, 'R': 12.4, 'H': 6}
    aa2chargeNeg = {'D': 3.86, 'E': 4.25, 'C': 8.33, 'Y': 10}
    aaNterm = 9.69
    aaCterm = 2.34
    aaDictionary = {}


    # the __init__ method requires a protein string to be provided, either as a
    # string or list of strings that will be concatenated
    def __init__(self, protein):
        l = ''.join(protein).split()
        self.protString = ''.join(l).upper()


    def aaCount(self):
        """ Iterates through every character in string and returns a count of valid 
        amino acids. Ignores invalid characters.
        Returns:
             aaTotal (int): Total number of valid amino acids.  
        """
        aaTotal = 0
        for i in self:                          # Iterates through each character in string object.
            if i.upper() in self.aa2mw.keys():  # Checks if character is valid by checking if it's in dictionary aa2mw.
                aaTotal += 1
        return aaTotal


    def pI(self):
        pass


    def aaComposition(self):
        """ Constructs dictionary consisting of amino acids as keys and the count of each one as values.
        Returns: A dictionary keyed by single letter amino acid code, having 
        associated values that are the counts of those amino acids in the sequence.
        """
        for i in self.aa2mw.keys():
            self.aaDictionary[i] = self.protString.count(i)
        return self.aaDictionary


    def _charge_(self):
        pass


    def molarExtinction(self):
        pass


    def massExtinction(self):
        myMW = self.molecularWeight()
        return self.molarExtinction() / myMW if myMW else 0.0


    def molecularWeight(self):
        """
        Calculates the MW of the protein sequence. 
        """
        aaWeight = 0
        waterMW = ProteinParam.mwH2O *(ProteinParam.aaCount(self) - 1)
        #for aa in ProteinParam.aaDictionary:
        #    aaWeight += (ProteinParam.aaDictionary.get(aa)*ProteinParam.aa2mw.get(aa))

        for aa, count in ProteinParam.aaDictionary.items():
            aaWeight += count * ProteinParam.aa2mw[aa]
        return aaWeight - waterMW

# Please do not modify any of the following.  This will produce a standard output that can be parsed
from pprint import pprint as pp
import sys


for inString in sys.stdin:
    myParamMaker = ProteinParam(inString)
    myAAnumber = myParamMaker.aaCount()
    myAAcomposition = myParamMaker.aaComposition()
    print("Number of Amino Acids: {aaNum}".format(aaNum=myAAnumber))
    print("Molecular Weight: {:.1f}".format(myParamMaker.molecularWeight()))
    #print("molar Extinction coefficient: {:.2f}".format(myParamMaker.molarExtinction()))
    #print("mass Extinction coefficient: {:.2f}".format(myParamMaker.massExtinction()))
    #print("Theoretical pI: {:.2f}".format(myParamMaker.pI()))
    #print("Amino acid composition:")
    #myAAcomposition = myParamMaker.aaComposition()
    #keys = list(myAAcomposition.keys())
    #keys.sort()
    #if myAAnumber == 0: myAAnumber = 1  # handles the case where no AA are present
    #for key in keys:
    #    print("\t{} = {:.2%}".format(key, myAAcomposition[key] / myAAnumber))