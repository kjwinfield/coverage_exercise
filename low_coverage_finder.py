#!/usr/bin/env python3
'''
This script takes the output table of coverage data from sambamba and generates
a list of genes that have less than 100% coverage at 30x 
'''
import pandas as pd


def find_low_coverage(file):
    '''
    Takes sambamba output coverage data and returns a dataframe of regions with
    less than 100% coverage at 30x
        inputs:
            file: coverage data table
        outputs:
            coverage_under_100 (dataframe): regions of sample with low coverage
    '''
    df = pd.read_table(file)
    coverage_under_100 = df.loc[df['percentage30'] < 100]

    return coverage_under_100


def returns_gene_list(table):
    '''
    Takes a dataframe of regions with low coverage and returns a list of genes
    that have low coverage
        inputs:
            table (dataframe): regions of sample with low coverage
        outputs:
            low_coverage (list): list of gene symbols that have low coverage
            regions
    '''
    genes_and_accessions = table['GeneSymbol;Accession'].unique()
    low_coverage = [x.split(';')[0] for x in genes_and_accessions]

    return low_coverage


def main():
    '''
    Call functions
    '''
    with open("/home/katherine/coverage_exercise/NGS148_34_139558_CB_CMCMD_S33_R1_001.sambamba_output.txt", 'r', encoding='utf-8') as file:
        low_coverage_exons = find_low_coverage(file)
        genes_with_low_coverage = returns_gene_list(low_coverage_exons)
        print(genes_with_low_coverage)

    with open("genes_with_low_coverage.txt", "w", encoding='utf-8') as f:
        genes_with_low_coverage = '\t'.join(genes_with_low_coverage)
        f.write(genes_with_low_coverage)


if __name__ == "__main__":
    main()
