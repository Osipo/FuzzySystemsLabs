#    Checking On Rules on http://www.attotron.com/cybertory/analysis/trans.htm
#
#    Complementary Sequence Of DNA:
#    http:/arep.med.harvard.edu/labgc/adnan/projects/Utilities/revcomp.htm
RulOfCon = {
    "A" : "T",
    "T" : "A",
    "G" : "C",
    "C" : "G"
}
def getAcids(f):
    f = open(f,'r',encoding='utf-8')
    k = ""
    d = dict()
    for line in f.readlines():
        i = 0
        while (i < len(line)):
            d[line[i:i+3]] = line[i+5:i+6] # format: LLL: L\n
            i+=6
    f.close()
    return d


TablesOfAcids = {"AUG" : "M","ACA" : "C","UGU" : "W","CCC":"*","AGA" : "S","UUC" : "Y","GCG" : "G", "GAA": "H","AAC" : "E","TGT" : "J", "TCT": "Z", "ACU" : "T", "GGA" : "G","UAA" :"*", "TUC" : "Q"}
def complementarySeq(strarg):
    i = 0; answer = ""
    for i,_ in enumerate(strarg):
        answer += RulOfCon[strarg[i]]
    return answer

def sequenceOfRNA(complDNASeq):
    answer = ""
    l = list(map(lambda x: 'U' if x == 'A' else RulOfCon[x],complDNASeq))
    for s in l:
        answer += s
    return answer

def process(fname):
    file = open(fname,'r',encoding='utf-8')
    result = ""
    for line in file.readlines():
        result += MapToAcids(sequenceOfRNA(complementarySeq(line)))
    file.close()
    return result

def MapToAcids(nuclstr):
    i = 0
    answer = "";
    while(i < len(nuclstr)):
        try:
            answer += TablesOfAcids[nuclstr[i:i+3]]
        except KeyError:
            answer +=""
        i+=3;
    return answer

ex = "ATGGAAACAAGATTCGCGTGTCCC"
print("Source : "+ex)
cex = complementarySeq(ex)
print("CDNA: "+cex)
rr = sequenceOfRNA(cex)
print("RNA: "+rr)
print("ACIDS: "+MapToAcids(rr))