

# Data

## data/breast-cancer-relapse-geo

Source: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=gse2034

Download the data:

    cd data
    mkdir breast-cancer-relapse-geo
    cd breast-cancer-relapse-geo
    curl -O https://ftp.ncbi.nlm.nih.gov/geo/series/GSE2nnn/GSE2034/soft/GSE2034_family.soft.gz

Extract the two primary tables from the root directory:

    zcat data/breast-cancer-relapse-geo/GSE2034_family.soft.gz | \
        python3 scripts/extract_soft_table.py - Data_matrix_for_GSE2034 | \
        gzip -c > data/breast-cancer-relapse-geo/GSE2034_genes.tsv.gz

    zcat data/breast-cancer-relapse-geo/GSE2034_family.soft.gz | \
        python3 scripts/extract_soft_table.py - Data_matrix_for_GSE2034 > \
        data/breast-cancer-relapse-geo/GSE2034_genes.tsv


This data is preprocessed in the [breast-cancer-geo-cleaning](notebooks/breast-cancer-geo-cleaning.ipynb) notebook.