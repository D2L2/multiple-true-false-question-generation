This project provides a Natural Language Pipeline for processing German Textbook sections as an input generating Multiple True-False Question using GPT2.


# Features
- generation of false statements
- automatic selection of true statements 
- selection of an arbitrary similarity for true and false statements as well as the number of false statements
- generating false statements by adding or deleting negations as well as using a german gpt2

# Setup

## Getting startet

1. After installation you need to execute the run.sh script by e.g. running `bash run.sh` in the terminal


## Installation

1. Create a new environment: `conda create -n mtfenv python=3.9`
2. Activate the environment: `conda activate mtfenv`
3. Install dependencies using anaconda: 
```
conda install -y -c conda-forge pdfplumber
conda install -y -c conda-forge nltk
conda install -y -c conda-forge pypdf2
conda install -y -c conda-forge pylatexenc
conda install -y -c conda-forge packaging
conda install -y -c conda-forge transformers
conda install -y -c conda-forge essential_generators
conda install -y -c conda-forge xlsxwriter
```
3. Download spacy: `python3.9 -m spacy download de_core_news_lg`

# Roadmap
[click here to see the roadmap](https://gitlab.pi6.fernuni-hagen.de/la-diva/adaptive-assessment/generationofmultipletruefalsequestions/-/blob/master/MTF-generation_Roadmap.png)

# License

Distributed under the MIT License. See [LICENSE.txt](https://gitlab.pi6.fernuni-hagen.de/la-diva/adaptive-assessment/generationofmultipletruefalsequestions/-/blob/master/LICENSE.txt) for more information.

# Contact
- Regina Kasakowskij (M.A.) - regina.kasakowskij@fernuni-hagen.de
- Dr. Niels Seidel - niels.seidel@fernuni-hagen.de

# Research
This project was carried out as part of research in the project LA-DIVA
Project Link: [Project page LA-DIVA](https://www.fernuni-hagen.de/forschung/schwerpunkte/catalpa/forschung/projekte/la-diva.shtml)

## Publications
[Kasakowskij, R., Kasakowskij, T. & Seidel, N., (2022). Generation of Multiple True False Questions. In: Henning, P. A., Striewe, M. & Wölfel, M. (Hrsg.), 20. Fachtagung Bildungstechnologien (DELFI). Bonn: Gesellschaft für Informatik e.V.. (S. 147-152). DOI: 10.18420/delfi2022-026](https://dl.gi.de/handle/20.500.12116/38826)

# Acknowledgments

This research was supported by CATALPA – Center of Advanced Technology for Assisted Learning and Predictive Analytics of the FernUniversität in Hagen, Germany.
