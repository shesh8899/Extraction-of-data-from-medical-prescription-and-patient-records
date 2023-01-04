import re
from medicaldocparser import medical_doc_parser
class patient(medical_doc_parser):
    def __init__(self,text):
        medical_doc_parser.__init__(self,text)

    def parse(self):
        return {
            "patient_name":self.get_patient_name(),
            "patient_number":self.get_phone(),
            "patient_vaccination":self.get_vaccination(),
            "other_diseases":self.other_issues()
        }

    def get_patient_name(self):
        pattern = 'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        name = ''
        if matches:
            name = self.remove_noise_from_name(matches[0])
        return name


    def remove_noise_from_name(self, name):
        name = name.replace('Birth Date', '').strip()
        date_pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)
        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name

    def get_phone(self):
        match = re.findall('Patient Information .*(\(\d{3}\) \d{3}-\d{4})',self.text, flags=re.DOTALL)
        return match[0]

    def get_vaccination(self):
        match = re.findall('Have you had the Hepatitis B vaccination\?(.*)List', self.text, flags=re.DOTALL)
        return match[0].strip()

    def other_issues(self):
        match = re.findall('List any Medical Problems \(asthma, seizures, headaches\}:(.*)', self.text, re.DOTALL)
        return match[0].strip()

if __name__=="__main__":
    tex='''17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 '

United States Height:
190

In Case of Emergency
ee J
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
nn i
Chicken Pox (Varicella): Measies:
IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches}:

Migraine'''
    p1= patient(tex)


