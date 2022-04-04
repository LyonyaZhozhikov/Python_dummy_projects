# NBAS subunit of NRZ tethering complex [Homo sapiens] NCBI Reference Sequence: NP_056993.2
from Bio import Entrez
NBAS = input('Please, type requested gene name: \n')
aa_dict_names = {'G': 'Glicin', 'A': 'Alanin', 'V': 'Valin', 'L': 'Leucine',
                'I': 'Isoleucine', 'P': 'Prolin', 'S': 'Serin', 'T': 'Treonin',
                'C': 'Cystein', 'M': 'Metionin', 'N': 'Asparagin', 'Q': 'Glutamin',
                'F': 'Phenilalanin', 'Y': 'Tyrosin', 'W': 'Triptofan',
                'D': 'Asparagin acid', 'E': 'Glutamin acid', 'K': 'Lysin',
                'R': 'Arginin', 'H': 'Histidine'}

Entrez.email = 'jlr10@mail.com'
handle = Entrez.esearch(db="protein", term=f"{NBAS} AND Homo sapiens[orgn]")
record = Entrez.read(handle)
Entrez.efetch(db="protein", id=record["IdList"], retmode="text", rettype="fasta").read()
prot_variants = []

for rec in record["IdList"]:
    lne = Entrez.efetch(db="protein",
                        id=rec,
                        retmode="text",
                        rettype="fasta").read()
    if f'{NBAS}' in lne:
        prot_variants.append(lne)
transcripts_list = []
n_count = 0
for i in prot_variants:
    m = i.split('\n')
    string_1 = ''
    for l in m:
        if '>' in l:
            transcripts_list.append(l)
        if '>' not in l:
            string_1 += l
    prot_variants[n_count] = string_1
    n_count += 1
transcripts_list_count = 0
for protein in prot_variants:
    # protein_straight = ""
    # for aa in protein:
    #     if aa == "\n":
    #         aa = ""
    #     else:
    #         protein_straight += aa
    aa_dict_count = {}
    for i in protein:
        if i not in aa_dict_count.keys():
            aa_dict_count[i] = 1
        elif i in aa_dict_count.keys():
            aa_dict_count[i] += 1

    sorted_aa_values = sorted(aa_dict_count.values())
    sorted_aa_dict = {}

    for i in sorted_aa_values:
        for k in aa_dict_count.keys():
            if aa_dict_count[k] == i:
                sorted_aa_dict[k] = aa_dict_count[k]
                break
    print(f'Sorted list of {transcripts_list[transcripts_list_count]} amminoacids:')
    for i in sorted_aa_dict:
        print(f"'{aa_dict_names[i]}' = ", aa_dict_count[i]/len(protein)*100)
    print('total aa count == ', len(aa_dict_count), '\n')
    transcripts_list_count += 1
