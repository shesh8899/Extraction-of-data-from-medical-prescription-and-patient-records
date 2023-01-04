import re
from medicaldocparser import medical_doc_parser
class prescription_parse(medical_doc_parser):
    def __init__(self,text):
        medical_doc_parser.__init__(self,text)

    def parse(self):
        return {
            "patient_name":self.get_name(),
            "patient_address":self.get_address(),
            "medicines":self.get_medicine(),
            "Directions":self.get_directions(),
            "Refills":self.get_refills()
        }

    def get_name(self):
        match=re.findall('Name:(.*)Date',self.text)
        if len(match)>0:
            return match[0].strip()

    def get_address(self):
        match = re.findall('Address:(.*)\n', self.text)
        if len(match) > 0:
            return match[0].strip()


    def get_medicine(self):
        match=re.findall('Address:[^\n]*(.*)Directions',self.text,flags=re.DOTALL)
        if len(match)>0:
            return match[0].strip()

    def get_directions(self):
        match=re.findall('Directions:(.*)Refill',self.text,flags=re.DOTALL)
        if len(match)>0:
            return match[0].strip()

    def get_refills(self):
        match = re.findall("Refill:(.*)times", self.text)
        if len(match) > 0:
            return match[0].strip()




doc_text='''
Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC


Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times'''
'''pres=prescription_parser(doc_text)
print(pres.parse())'''

p1 = prescription_parse(doc_text)
