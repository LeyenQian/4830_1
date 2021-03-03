#!/usr/bin/python3

import sys
#import numpy as np
from collections import Counter

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

index = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}

character = {
    0:'A',
    1:'B',
    2:'C',
    3:'D',
    4:'E',
    5:'F',
    6:'G',
    7:'H',
    8:'I',
    9:'J',
    10:'K',
    11:'L',
    12:'M',
    13:'N',
    14:'O',
    15:'P',
    16:'Q',
    17:'R',
    18:'S',
    19:'T',
    20:'U',
    21:'V',
    22:'W',
    23:'X',
    24:'Y',
    25:'Z'
}
def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    #print(s)
    freqs = Counter(s)
    #print(freqs)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    #print(mean*len(freqs))
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

def std_var():
    """Calculate the population variance of letter frequencies in given string."""
    #print(freqs)
    mean = sum(float(v) for v in letter_freqs.values())/len(letter_freqs)  
    #print(mean*len(freqs))
    return sum((float(letter_freqs[c])-mean)**2 for c in letter_freqs)/len(letter_freqs)

def encript(text, key):
    length = len(key)
    l = 0
    ciphered_text = ""
    for i in text:
        ciphered_text = ciphered_text + character[(index[i]+index[key[l]])%26]
        l = (l+1)%length
    return ciphered_text


def pop_var2(s, l_key):
    ss = []
    for i in range(l_key):
        if i >= len(s):
            break
        substring = ""
        j = i
        while(j < len(s)):
            substring = substring + s[j]
            j = j + l_key
        ss.append(substring)
    variances = []
    #print(ss)
    for i in ss:
        variances.append(pop_var(i))
    return sum(variances)/len(variances)


if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()

    #################################################################
    # Your code to determine the key and decrypt the ciphertext here
    p = False
    if p:
        paintext = "ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper"
        paintext = paintext.upper()
        print("population variance paintext:",pop_var(paintext))


        key1 = "YZ"
        ciphered_text1 = encript(paintext, key1)
        #print(ciphered_text1)
        print("population variance of key = "+key1+":",pop_var(ciphered_text1))


        key2 = "XYZ"
        ciphered_text2 = encript(paintext, key2)
        #print(ciphered_text2)
        print("population variance of key = "+key2+":",pop_var(ciphered_text2))


        key3 = "WXYZ"
        ciphered_text3 = encript(paintext, key3)
        #print(ciphered_text3)
        print("population variance of key = "+key3+":",pop_var(ciphered_text3))


        key4 = "VWXYZ"
        ciphered_text4 = encript(paintext, key4)
        #print(ciphered_text4)
        print("population variance of key = "+key4+":",pop_var(ciphered_text4))


        key5 = "UVWXYZ"
        ciphered_text5 = encript(paintext, key5)
        #print(ciphered_text5)
        print("population variance of key = "+key5+":",pop_var(ciphered_text5))


        print(pop_var2(ciphered_text5,6))

    #------------------------------------
    # determine the size of the key:
    #------------------------------------

    # cipher = "YODFARFVSXLCOIESCQMDPVNNFDYFCRQVNKGMAOKACEYIZXQXMOAJWNOIABBSIWAXZKYOKQFHHFHFIDUIWQRZWFAOYMXODXRHHXHRBDMPJACQMOWKBHHBPBAGHDMRCRNCWQAZHWARQDXOKZMLJMKJGRYNAZSQCOUEMVYQAOSRCICQFNMZPBAGHDMRCRCIPECQYVHTMQFYIXWUCJHXRDNCAIYVIMPECTHDRBPRCOUPPTFZOXLCCOIXWAYPJBRGCXWISMXZNPMLYXEOATGNPXLBYNASCMJMKYGMAAKOUDUFJBQRYNIXWQYNQIRHHNASCQYKAKYKNDAPSONJWKBHHXHRBHHBAUNTFNELLBCQEIDHHZOXLCDVEIRHGZKRPOIGEZWHHZAZQHMODXRXIPIRQSLZOMCBNODBNQCQWZWZHYLOMOYMPVPHACPPMEIODBPRUOWIJSCHAPMQYGOBWNOREIJEUDHQFDWJQOQDUXPFLFFVSCSKFTWKBDNCEZYKFTEPWNOMNBQOIIOFZHFDPVAZLZBRJKSMAXBSBZYLKOOOAODQUPZXLCUWQPCZWOYCYZUAAACQUGOQYSOOAQFZNWNLYCFTYOGLCIWIGYYNYLKOOOAOGMNMQPGNHODFQHMJJBMEMZRBPZFGWTQSBVPDMUYMJEYBEDJDSMXZNPRZHYSEYSNCAIYVJMKEGACOOFDHHYKRZSQZYXLQYAAOWNOOKXLZNOKOLDSKHBYRYMASGDQDPPQOIGEZGDMJJOCRJJJPGAFZQPCNZOAZFMIGKDWQYNKRPBYNWKBBUZJPNNFDYVBNWPIBLSMAKOETCYAIGMYNYLLBYMJFLFJMKMCQ"

    # cipher = "MOFTLYYPCALEPHOOOGTUXJCNXRIHVDFTCRLCFTBTJTTYOMTBPBCDLMRBUHALTBPBCDLSVEWPRMHNMUSERTHKOPDMHRBSPYXSLHVDEXMGHILVXAYHUEOLALKFXAKKRWTTLOEELQTTMIAZGLRBNGHUSETIEIJAENPNGEWEMMRAFLRBTBKMLYMONQZZUKPNKEZNLIEKFEUKNRWPYEHFGAFXEGYBNSPPKEGMZQRXEJBUSSHMRHGEHXRHEFDMTYOXZZUELXBOOLRKRXQLNXYRNQZNMHRKFDTMHVLDCEPSQBTDAMIFYJPDMHVLDCEPDBGUGAELLUVWLRIAZBXAKLVGTAIDEGAJDCKEJABDIMSEBHSTLLVDFZTAEEVSPWLIYENLKXSBYSPETSGABEAGDORZZUKOJGSFLXSVMBVEBTJXDLNMAYDUZGXTUXSTAQYBNSAAKDBGTTRTCXGPHLXDTBORYHUSHSEOUEPTQEABNTTUEHBSCKFDEGTONUTCEAVFNJRBGUMBYDLTRITZUMSVWFQOKAPHVYCBLNGEHIMHNGFWAUOETUPSXAFTMFTXTUBTQEELBPBWOGGVEMWOHKVGHJEELBPFJEWMNGPQFBVRTOOTAIEMZDTXPCXENOHLYRUZWTRQLUSEWOBKBYDWIFTQAETRRWPFTHFGAFSONSRHOPAYTRKBYOMHRKUSEKEFMGZLEOJXESILEKTNALXENVIXADIAZBDAEUGXBDHXPNLTPDXAPABODBNTLPXETPBEPRYTCPHSOIGGGHSFLXSFTJOOGESHSPCTSGEFNONNPBMDABDZHSRAGAAWTZWBTUHOPRXMNKLZRTNBMIPRTLYFBCCAEQHVEAGDYXGESBLIXSLNWMRTMZNXWVMIEHXTBKDSTAEFXBNOHKVGTEAGTYRSPMHVRWITSIICXOZWEOBDZZUAEEXKTMAAJDJYSAEFTJOIGAFMFLDRWUBTAEKTUTUHALNBFPCEMHNGBFDBBYXZZUKEJBUSIGHNEGLPEAADPQDXAGABYDPHNMTLLHNTLJRHMWBKTPOYTBKUFRXTUXZCEZOVGHEOMHEHXXEHFSUVEYHUZTSVILTNGEMYROHMICONGUMITCDAAWUSIGIQBEYTFENGUZNHNBMUTLEYBNTAODEHIJHALAOHVEDXSCXSLTXTBEPDEMHNMNFCABYNOEAGDOXILNZEQBOEOMHRUBCGTIAUVEILERRPFWTSGAFCIZHGLPCTBSNRTEOFYFXMQYHUFMBYDUYUTXVIGSWHIYAGDUTXVIGSYETEAGDORZZUROHKFSILLNLUNAKDNGEMYMHREJGIGGGAVYDXRWHIYHXSLHVCSUAPDUZBTCXLBJSBYBNTLVXYBNSHIMNRLTLNWHREMDAOELHVCNXCXBCPGTNQBNWYMOHGEPRLTNGEJONMRTOLLESYHTEITSXXELYXBLZVXIWOUXBYSPEEXEDHBPTHOPNXCXZPYEMHNMTEHXSVSFZFBTBGDPIEOBDFOIGTBMILTUALCJXHTWXBODAGDFXFYNHSPAPZNXRJXMWIFTBNHSBNTVZBGEHUGTTQOKTUTUWOMAAWUSEBRPHVYCBLZTSVMXTUXZCEHUGKJRHMFBHMDAGDPHXLRWSVEMDAOELHVCLBFRBGDOUENLJNAGFEHNEHXMONUDEXHRKFUIFTVMGZRMAGRPFSTVREPYGCOUGGCOFSJBORIGGVPBDBXWVEEPRXDVMTPEFEQTUSIGGFHIZPXLRLTSEPAFTTVIGGUXUSEHLQUVNCTNRXSEHXRVGHWETDRKUSRHUTAPFTPHNMJNAGDBMILTBLYWPTSTIQBUDAUAEZBTNVRVXEWOGGWHIYYHUFIFLKNPCEVNKRAAWCJTAUAWFCIOENVILNVEUXIZBULRWUZTAEGHSNHPHRKFTTLTBHEARHPCXELMHNTMIPFBRRPPZDTNQMPZKTFEXTSLBGUMUZHBSCBQPUGDRKTEAGDZXKTMAEFTJORXTHKOTNZIIXBSETDBGNJSAOHEEPRLIUTWPIFOALRFIKEFLJOEGOJBLYOPYBNWPGHTGABESA"
    
    variances = []

    standard_var = std_var()

    #print("Standard Variance = ", standard_var)

    for i in range(2, 14):
        variances.append(pop_var2(cipher,i))

    #variances = np.array(variances)
    variances_differences = []
    for i in variances:
        variances_differences.append(abs(i - standard_var))
    #print(variances_differences, variances)

    key_length = variances_differences.index(min(variances_differences))+2

    if p:
        print("Key length = ",key_length)


    substrings = []
    for i in range(key_length):
        substring = ""
        j = i
        while(j < len(cipher)):
            substring = substring + cipher[j]
            j = j + key_length
        substrings.append(substring)

    ss_matrix = []
    for i in substrings:
        ss_vector = []
        for j in range(0, 26):
            ss_vector.append(encript(i, character[j]))
        ss_matrix.append(ss_vector)
    #print(ss_matrix)

    key_solutions = []

    for i in ss_matrix:
        key_solution = []
        for j in i:
            frequency = Counter(j)
            temp = 0
            for k in alphabet:
                temp = temp + abs(frequency[k]/len(j) - letter_freqs[k])
            key_solution.append(temp)
        #print(key_solution)
        key_solutions.append(key_solution.index(min(key_solution)))

    if p:
        print("decipher keys in numbers:",key_solutions)

    decipher_key_string = ""
    key_string = ""

    for i in key_solutions:
        key_string = key_string + character[(26-i)%26]
        decipher_key_string = decipher_key_string + character[i]

    print(key_string)
    if p:
        print(encript(cipher, decipher_key_string))