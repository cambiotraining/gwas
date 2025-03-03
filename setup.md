---
title: "Data & Setup"
number-sections: false
---

<!-- 
Note for Training Developers:
We provide instructions for commonly-used software as commented sections below.
Uncomment the sections relevant for your materials, and add additional instructions where needed (e.g. specific packages used).
Note that we use tabsets to provide instructions for all three major operating systems.
-->

::: {.callout-tip level=2}
## Workshop Attendees

If you are attending one of our workshops, we will provide a training environment with all of the required software and data.  
If you want to setup your own computer to run the analysis demonstrated on this course, you can follow the instructions below.
:::

## Data

The data used in these materials is provided as a zip file. 
Download and unzip the folder to your Desktop to follow along with the materials.

<!-- Note for Training Developers: add the link to 'href' -->
<a href="https://www.dropbox.com/scl/fo/vnriegyd1kr1hgfkcb3nk/AKVJc6CcC_-bwYeLGIMbYFs?rlkey=4mmt6zc9u3ap1z6k7w1lwgmyu&st=8sva9t9r&dl=1">
  <button class="btn"><i class="fa fa-download"></i> Download</button>
</a>

## Software

We use the **Mamba** package manager to install the necessary software. 

See our separate software installation instructions page for [how to install Mamba](https://cambiotraining.github.io/software-installation/materials/mamba.html). 
**Windows** users are recommended to [install WSL](https://cambiotraining.github.io/software-installation/materials/wsl.html) and follow the instructions for Linux.

Then, create a Mamba environment with the required packages:

```bash
mamba create -n gwas plink2 gcta gemma bcftools gsl
```