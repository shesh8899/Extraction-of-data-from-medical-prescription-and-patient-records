from src.presciption_parser import prescription_parse
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
def test_name(text):
    pp1=prescription_parser(text)
    assert pp1.parse()