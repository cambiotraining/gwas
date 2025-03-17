---
title: "Genome-Wide Association Studies (GWAS)"
pagetitle: "GWAS"
date: today
number-sections: false
---

## Overview 

Genome-Wide Association Studies (GWAS) investigate the genetic basis of complex traits and/or diseases.
These materials cover the bioinformatic and statistical methods required to identify associations between genetic variants and traits. 
You will learn to use essential software for genotype data processing, including quality control crucial for downstream analysis. 
We discuss how population ancestry may impact association results and how this can be adjusted for in the analysis.
We introduce key statistical concepts relevant to GWAS, with applications to both quantitative and binary traits. 
Finally, we introduce methods to assess potential biases in GWAS results and demonstrate how to generate effective visualisations.

::: {.callout-tip}
### Learning Objectives

- Describe key concepts, advantages and limitations of GWAS.
- Use PLINK to generate key metrics for quality control of samples and variants. 
- Recognise the effect of population structure when performing association tests and how to adjust for it. 
- Summarise the statistical methods used for association analysis and how to interpret their outcomes. 
- Run a GWAS for quantitative and binary traits and assess the quality of the results. 
- Visualise and report the findings of the association analysis. 
:::


### Target Audience

Researchers and students interested in the genetics of complex traits. 


### Prerequisites

- Knowledge of key genetics concepts and terms, such as: gene, locus, allele, linkage, inheritance, homozygous and heterozygous genotypes.
  - See [NIH's genetics glossary](https://www.genome.gov/genetics-glossary) for reference.
- Knowledge of basic statistical concepts, such as: linear regression, null hypothesis testing, p-value, effect size. Knowledge of logistic regression is also desirable. 
  - See our [Core Statistics](https://cambiotraining.github.io/corestats/) and [Generalised Linear Models](https://cambiotraining.github.io/stats-glm/) materials as a reference. 
- Basic usage of the Unix command line: listing files (`ls`), moving between directories (`cd`) and an understanding of using options/flags with commands (e.g. `command --input file.csv --output result.csv`).
  - See the "Basics" section of our [Introduction to Unix command line](https://cambiotraining.github.io/unix-shell/) materials.
- Using R and the `tidyverse` package for data exploration and visualisation. 

<!-- Training Developer note: comment the following section out if you did not assign levels to your exercises -->
<!-- ### Exercises

Exercises in these materials are labelled according to their level of difficulty:

| Level | Description |
| ----: | :---------- |
| {{< fa solid star >}} {{< fa regular star >}} {{< fa regular star >}} | Exercises in level 1 are simpler and designed to get you familiar with the concepts and syntax covered in the course. |
| {{< fa solid star >}} {{< fa solid star >}} {{< fa regular star >}} | Exercises in level 2 combine different concepts together and apply it to a given task. |
| {{< fa solid star >}} {{< fa solid star >}} {{< fa solid star >}} | Exercises in level 3 require going beyond the concepts and syntax introduced to solve new problems. | -->


## Citation & Authors

Please cite these materials if:

- You adapted or used any of them in your own teaching.
- These materials were useful for your research work. For example, you can cite us in the methods section of your paper: "We carried our analyses based on the recommendations in _YourReferenceHere_".

<!-- 
This is generated automatically from the CITATION.cff file. 
If you think you should be added as an author, please get in touch with us.
-->

{{< citation CITATION.cff >}}


## Acknowledgements

<!-- if there are no acknowledgements we can delete this section -->

- List any other sources of materials that were used.
- Or other people that may have advised during the material development (but are not authors).
