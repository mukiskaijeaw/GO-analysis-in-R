genes = """KRAS
LHX1
ARHGDIA
TMEM218
"""

gene_list = genes.split()

output = ", ".join(f'"{gene}"' for gene in gene_list)


print(output)
