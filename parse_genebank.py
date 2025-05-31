#!/usr/bin/env python3

import re, argparse, sys, io

parser = argparse.ArgumentParser(
    prog="pgb",
    description='''
    Parse GeneBank records''',
    epilog="M.Hryc (2025)"
)
parser.add_argument(
    "-i", "--input",
    required=True,
    type=str,
    help='''
Path to input file'''
)
parser.add_argument(
    "-r", "--record",
    type=int, default=0,
    help='''
Index (0 based) of the record to print'''
)
parser.add_argument(
    "-f", "--field",
    type=str, default="origin",
    help='''
Pick which field of the record to show, options: locus, definition, accession,
version, keywords, source, organism, comment, features, origin'''
)

def split_records(infile: str) -> [str]:
    gb_file = []
    with open(infile, 'r') as f:
        record = []
        for line in f:
            if not (line == "//\n" or line == "//"):
                record.append(line)
            else:
                gb_file.append(''.join(record))
                record.clear()

    return gb_file

def parse_source(inlist):
    return
def parse_origin(inlist):
    parsed_list = []
    for line in inlist:
        parsed_list.append(line.translate(str.maketrans('', '', " 0123456789")))

    return ''.join(parsed_list)

def parse_record(inrecord: str):
    record_structure = {
        "LOCUS": [],
        "DEFINITION": [],
        "ACCESSION": [],
        "VERSION": [],
        "KEYWORDS": [],
        "SOURCE": [],
        "ORGANISM": [],
        "REFERENCE": [],
        "COMMENT": [],
        "FEATURES": [],
        "ORIGIN": []
    }
    keys, record = [key for key in record_structure.keys()], inrecord.split('\n')

    key_idx = 0
    for line in record:
        try:
            if keys[key_idx + 1] in line:
                key_idx += 1
                #print(keys[key_idx])
        except IndexError:
            pass

        record_structure[keys[key_idx]]\
            .append(
                line.replace(keys[key_idx], "").strip()
            )
    record_structure["LOCUS"] = record_structure["LOCUS"][0]
    record_structure["DEFINITION"] = ''.join(record_structure["DEFINITION"])
    record_structure["ACCESSION"] = record_structure["ACCESSION"][0]
    record_structure["VERSION"] = ''.join(record_structure["VERSION"])
    record_structure["KEYWORDS"] = ''.join(record_structure["KEYWORDS"])
    record_structure["SOURCE"] = record_structure["SOURCE"][0] + '\n'
    record_structure["ORGANISM"] = ''.join(record_structure["ORGANISM"]) + '\n'
#    record_structure["REFERENCE"] =
    record_structure["COMMENT"] = ''.join([line + '\n' for line in record_structure["COMMENT"]])
    record_structure["FEATURES"] = ''.join([line + '\n' for line in record_structure["FEATURES"]])
    record_structure["ORIGIN"] = parse_origin(record_structure["ORIGIN"])

    return record_structure

if __name__ == "__main__":
    args = parser.parse_args()
    args.field = args.field.upper()

    gb_records = split_records(args.input)
    #sys.stdout.write(gb_records[-1])
    sys.stdout.write(
        parse_record(gb_records[args.record])[args.field]
    )
    #print(parse_record(gb_records[0])['ORIGIN'])

#LOCUS       WP_272867249             554 aa            linear   BCT 27-JUL-2024
#DEFINITION  ABC transporter ATP-binding protein [Bacillus massiliigorillae].
#ACCESSION   WP_272867249
#VERSION     WP_272867249.1
#KEYWORDS    RefSeq.
#SOURCE      Bacillus massiliigorillae
#  ORGANISM  Bacillus massiliigorillae
#            Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Bacillaceae;
#            Bacillus.
#
#COMMENT     REFSEQ: This record represents a single, non-redundant, protein
#            sequence which may be annotated on many different RefSeq genomes
#            from the same, or different, species.
#            
#            ##Evidence-For-Name-Assignment-START##
#            Evidence Category  :: Conserved Domain (CDD)
#            Evidence Accession :: Domain architecture ID 11438555
#            Evidence Source    :: NCBI SPARCLE
#            ##Evidence-For-Name-Assignment-END##
#            COMPLETENESS: full length.
#FEATURES             Location/Qualifiers
#     source          1..554
#                     /organism="Bacillus massiliigorillae"
#                     /db_xref="taxon:1243664"
#     Protein         1..554
#                     /product="ABC transporter ATP-binding protein"
#                     /EC_number="7.-.-.-"
#                     /GO_component="GO:0055052 - ATP-binding cassette (ABC)
#                     transporter complex, substrate-binding subunit-containing
#                     [Evidence IEA]"
#                     /GO_function="GO:0140359 - ABC-type transporter activity
#                     [Evidence IEA]; GO:0005524 - ATP binding [Evidence IEA];
#                     GO:0016887 - ATP hydrolysis activity [Evidence IEA];
#                     GO:0042626 - ATPase-coupled transmembrane transporter
#                     activity [Evidence IEA]"
#                     /calculated_mol_wt=60842
#     Region          1..545
#                     /region_name="MdlB"
#                     /note="ABC-type multidrug transport system, ATPase and
#                     permease component [Defense mechanisms]; COG1132"
#                     /db_xref="CDD:440747"
#ORIGIN      
#        1 msiittlvsl liplmtkelv dgfsmsslsw kqicliiavf ivqallsaya tyalsyngqk
#       61 iiaglrellw kkliklpvsy sdrngsgemi srmtndtmvv kelitthitg avtgiisvig
#      121 siiilfvmnw kltmlifivl plaalilvpi grlmhsiske tqaetatftg ilnqvlpeir
#      181 lvkafnaedi efnrgmkgis klfklglkea rtqslvgpiv tlvlmgalva vigyggmqvs
#      241 sgvisagslv afilylfqii mpmgqitvff tqlqksigat driveilate eedlqagktl
#      301 snakqsiifn dvtfayeege tilshidlki eagkvtaivg psgsgkttlf klleryylps
#      361 egrieigseq lndfslqswr nhigyvsqes pllagtirdn icygldrevt anelkkaaqm
#      421 ayaldfieel peqfntevge rglklsggqr qriaiarall rdpeilmlde atssldsqse
#      481 qsvqmaldql mvdrttivia hrlstvvdad qlvflekgvi tgigthselm kshalyrefa
#      541 qqqlkinsel vekv
#

#LOCUS       SCU49845     5028 bp    DNA             PLN       21-JUN-1999
#DEFINITION  Saccharomyces cerevisiae TCP1-beta gene, partial cds, and Axl2p
#            (AXL2) and Rev7p (REV7) genes, complete cds.
#ACCESSION   U49845
#VERSION     U49845.1  GI:1293613
#KEYWORDS    .
#SOURCE      Saccharomyces cerevisiae (baker's yeast)
#  ORGANISM  Saccharomyces cerevisiae
#            Eukaryota; Fungi; Ascomycota; Saccharomycotina; Saccharomycetes;
#            Saccharomycetales; Saccharomycetaceae; Saccharomyces.
#REFERENCE   1  (bases 1 to 5028)
#  AUTHORS   Torpey,L.E., Gibbs,P.E., Nelson,J. and Lawrence,C.W.
#  TITLE     Cloning and sequence of REV7, a gene whose function is required for
#            DNA damage-induced mutagenesis in Saccharomyces cerevisiae
#  JOURNAL   Yeast 10 (11), 1503-1509 (1994)
#  PUBMED    7871890
#REFERENCE   2  (bases 1 to 5028)
#  AUTHORS   Roemer,T., Madden,K., Chang,J. and Snyder,M.
#  TITLE     Selection of axial growth sites in yeast requires Axl2p, a novel
#            plasma membrane glycoprotein
#  JOURNAL   Genes Dev. 10 (7), 777-793 (1996)
#  PUBMED    8846915
#REFERENCE   3  (bases 1 to 5028)
#  AUTHORS   Roemer,T.
#  TITLE     Direct Submission
#  JOURNAL   Submitted (22-FEB-1996) Terry Roemer, Biology, Yale University, New
#            Haven, CT, USA
#FEATURES             Location/Qualifiers
#     source          1..5028
#                     /organism="Saccharomyces cerevisiae"
#                     /db_xref="taxon:4932"
#                     /chromosome="IX"
#                     /map="9"
#     CDS             <1..206
#                     /codon_start=3
#                     /product="TCP1-beta"
#                     /protein_id="AAA98665.1"
#                     /db_xref="GI:1293614"
#                     /translation="SSIYNGISTSGLDLNNGTIADMRQLGIVESYKLKRAVVSSASEA
#                     AEVLLRVDNIIRARPRTANRQHM"
#     gene            687..3158
#                     /gene="AXL2"
#     CDS             687..3158
#                     /gene="AXL2"
#                     /note="plasma membrane glycoprotein"
#                     /codon_start=1
#                     /function="required for axial budding pattern of S.
#                     cerevisiae"
#                     /product="Axl2p"
#                     /protein_id="AAA98666.1"
#                     /db_xref="GI:1293615"
#                     /translation="MTQLQISLLLTATISLLHLVVATPYEAYPIGKQYPPVARVNESF
#                     TFQISNDTYKSSVDKTAQITYNCFDLPSWLSFDSSSRTFSGEPSSDLLSDANTTLYFN
#                     VILEGTDSADSTSLNNTYQFVVTNRPSISLSSDFNLLALLKNYGYTNGKNALKLDPNE
#                     VFNVTFDRSMFTNEESIVSYYGRSQLYNAPLPNWLFFDSGELKFTGTAPVINSAIAPE
#                     TSYSFVIIATDIEGFSAVEVEFELVIGAHQLTTSIQNSLIINVTDTGNVSYDLPLNYV
#                     YLDDDPISSDKLGSINLLDAPDWVALDNATISGSVPDELLGKNSNPANFSVSIYDTYG
#                     DVIYFNFEVVSTTDLFAISSLPNINATRGEWFSYYFLPSQFTDYVNTNVSLEFTNSSQ
#                     DHDWVKFQSSNLTLAGEVPKNFDKLSLGLKANQGSQSQELYFNIIGMDSKITHSNHSA
#                     NATSTRSSHHSTSTSSYTSSTYTAKISSTSAAATSSAPAALPAANKTSSHNKKAVAIA
#                     CGVAIPLGVILVALICFLIFWRRRRENPDDENLPHAISGPDLNNPANKPNQENATPLN
#                     NPFDDDASSYDDTSIARRLAALNTLKLDNHSATESDISSVDEKRDSLSGMNTYNDQFQ
#                     SQSKEELLAKPPVQPPESPFFDPQNRSSSVYMDSEPAVNKSWRYTGNLSPVSDIVRDS
#                     YGSQKTVDTEKLFDLEAPEKEKRTSRDVTMSSLDPWNSNISPSPVRKSVTPSPYNVTK
#                     HRNRHLQNIQDSQSGKNGITPTTMSTSSSDDFVPVKDGENFCWVHSMEPDRRPSKKRL
#                     VDFSNKSNVNVGQVKDIHGRIPEML"
#     gene            complement(3300..4037)
#                     /gene="REV7"
#     CDS             complement(3300..4037)
#                     /gene="REV7"
#                     /codon_start=1
#                     /product="Rev7p"
#                     /protein_id="AAA98667.1"
#                     /db_xref="GI:1293616"
#                     /translation="MNRWVEKWLRVYLKCYINLILFYRNVYPPQSFDYTTYQSFNLPQ
#                     FVPINRHPALIDYIEELILDVLSKLTHVYRFSICIINKKNDLCIEKYVLDFSELQHVD
#                     KDDQIITETEVFDEFRSSLNSLIMHLEKLPKVNDDTITFEAVINAIELELGHKLDRNR
#                     RVDSLEEKAEIERDSNWVKCQEDENLPDNNGFQPPKIKLTSLVGSDVGPLIIHQFSEK
#                     LISGDDKILNGVYSQYEEGESIFGSLF"
#ORIGIN
#        1 gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg