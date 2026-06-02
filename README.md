# D-Lab Python NLP Fundamentals Workshop

[![Datahub](https://img.shields.io/badge/launch-datahub-blue)](https://dlab.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fdlab-berkeley%2FPython-NLP-Fundamentals&urlpath=lab%2Ftree%2FPython-NLP-Fundamentals%2F&branch=main)
[![Binder](https://img.shields.io/badge/launch-binder-579aca.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/dlab-berkeley/Python-NLP-Fundamentals/HEAD)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains the materials for the D-Lab Python NLP Fundamentals
workshop. 

## Prerequisites

We recommend attending Python Fundamentals, Python Data Wrangling, and
Python Machine Learning Fundamentals prior to this workshop.

Check out D-Lab’s [Workshop Catalog](https://dlab-berkeley.github.io/dlab-workshops/) to browse all workshops, see what’s running now, and review prerequisites.

## Workshop Goals

This 3-part workshop will prepare participants to move forward with research using Natural Language Processing (NL), with a special focus on social science applications. We explore fundamental approaches to applying computational methods to text in Python. We cover some of the major packages used in NLP, including scikit-learn, NLTK, spaCy, and Gensim.

1. **Part 1: Preprocessing.** How do we standardize and clean text
   documents? Text data is noisy, and we often need to develop a pipeline in
   order to standardize the data to better facilitate computational modeling. You will learn common and task-specific operations of preprocessing, 
   becoming familiar with commonly used NLP packages and what they are capable of. You will also learn about tokenizers,
   and how they have changed since the advent of Large Language Models.
2. **Part 2: Bag-of-words.** In order to do any computational analysis on text data, we need to devise approaches to convert text into a 
   numeric representation. You will learn how to convert text data to a frequency matrix, and how TF-IDF complements the Bag-of-Words representation.
   You will also learn about parameter settings of a vectorizer and apply sentiment classification to vectorized text data.
3. **Part 3: Word Embeddings.** Word Embeddings underpin nearly all modern language models. In this workshop, you will learn the differences 
   between a bag-of-words representation and word embeddings. You will be introduced to calculating cosine similarity between words, and learn how 
   word embeddings can suffer from biases.

The materials for this workshop series are designed to build on each other. Part 2 assumes familiarity with the content from Part 1, and Part 3 similarly requires understanding of both preceding parts.


## Installation Instructions

Anaconda is a useful package management software that allows you to run Python
and Jupyter notebooks easily. Installing Anaconda is the easiest way to make
sure you have all the necessary software to run the materials for this workshop.
If you would like to run Python on your own computer, complete the following
steps prior to the workshop:

1. [Download and install Anaconda (Python 3.9
   distribution)](https://www.anaconda.com/products/individual). Click the
   "Download" button.

2. Download the Python Text Analysis [workshop
   materials](https://github.com/dlab-berkeley/Python-NLP-Fundamentals):

   -   Click the green "Code" button in the top right of the repository
        information.
   -   Click "Download Zip".
   -   Extract this file to a folder on your computer where you can easily
        access it (we recommend Desktop).

3. Optional: if you're familiar with `git`, you can instead clone this
   repository by opening a terminal and entering the command `git clone
   git@github.com:dlab-berkeley/Python-NLP-Fundamentals.git`.

## Is Python Not Working on Your Laptop? 

If you do not have Anaconda installed and the materials loaded on your workshop
by the time it starts, we *strongly* recommend using the D-Lab Datahub to
run the materials for these lessons. You can access the DataHub by clicking the
following button:

[![Datahub](https://img.shields.io/badge/launch-datahub-blue)](https://dlab.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fdlab-berkeley%2FPython-NLP-Fundamentals&urlpath=lab%2Ftree%2FPython-NLP-Fundamentals%2F&branch=main)

The DataHub downloads this repository, along with any necessary packages, and
allows you to run the materials in a Jupyter notebook that is stored on UC
Berkeley's servers. No installation is necessary from your end - you only need
an internet browser and a CalNet ID to log in. By using the DataHub, you can
save your work and come back to it at any time. When you want to return to your
saved work, just go straight to [DataHub](https://datahub.berkeley.edu), sign
in, and you click on the `Python-NLP-Fundamentals` folder.

If you don't have a Berkeley CalNet ID, you can still run these lessons in the
cloud, by clicking this button:

[![Binder](https://img.shields.io/badge/launch-binder-579aca.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/dlab-berkeley/Python-NLP-Fundamentals/HEAD)

Binder operates similarly to the D-Lab DataHub, but on a different set of
servers. By using Binder, however, you cannot save your work.

## Run the Code

Now that you have all the required software and materials, you need to run the
code.

1. Open the Anaconda Navigator application. You should see the green snake logo
   appear on your screen. Note that this can take a few minutes to load up the
   first time. 

2. Click the "Launch" button under "JupyterLab" and navigate through your file
   system on the left hand pane to the `Python-NLP-Fundamentals` folder you
   downloaded above. Note that, if you download the materials from GitHub, the
   folder name may instead be `Python-NLP-Fundamentals-main`.

3. Go to the `lessons` folder and find the notebook corresponding to the
   workshop you are attending.

4. Press Shift + Enter (or Ctrl + Enter) to run a cell.

5. You will need to install additional packages depending on which workshop you
   are attending. The install commands are performed in the notebooks, as you
   proceed through each part of the workshop.

Note that all of the above steps can be run from the terminal, if you're
familiar with how to interact with Anaconda in that fashion. However, using
Anaconda Navigator is the easiest way to get started if this is your first time
working with Anaconda.

# Additional Resources

-  [Computational Text Analsysis Working Group (CTAWG)](http://dlabctawg.github.io)
-  [Info 256: Applied Natural Language Processing](https://www.ischool.berkeley.edu/courses/info/256)
-  [*Speech and Language Processing*](https://web.stanford.edu/~jurafsky/slp3/) by Jurafsky and Martin.
-  [Modern Deep Learning Techniques Applied to Natural Language Processing](https://nlpoverview.com/index.html) (online textbook)

# About the UC Berkeley D-Lab

D-Lab works with Berkeley faculty, research staff, and students to advance
data-intensive social science and humanities research. Our goal at D-Lab is to
provide practical training, staff support, resources, and space to enable you to
use R for your own research applications. Our services cater to all skill levels
and no programming, statistical, or computer science backgrounds are necessary.
We offer these services in the form of workshops, one-to-one consulting, and
working groups that cover a variety of research topics, digital tools, and
programming languages.  

Visit the [D-Lab homepage](https://dlab.berkeley.edu/) to learn more about us.
You can view our [calendar](https://dlab.berkeley.edu/events/calendar) for
upcoming events, learn about how to utilize our
[consulting](https://dlab.berkeley.edu/consulting) and [data
services](https://dlab.berkeley.edu/data), and check out upcoming
[workshops](https://dlab.berkeley.edu/events/workshops). Subscribe to our
[newsletter](https://dlab.berkeley.edu/news/weekly-newsletter) to stay up to
date on D-Lab events, services, and opportunities.

# Other D-Lab Python Workshops

D-Lab offers a variety of Python workshops, catered toward different levels of
expertise.

## Introductory Workshops

-  [Python Fundamentals](https://github.com/dlab-berkeley/Python-Fundamentals)
-  [Python Data Wrangling](https://github.com/dlab-berkeley/Python-Data-Wrangling)
-  [Python Data Visualization](https://github.com/dlab-berkeley/Python-Data-Visualization)

## Intermediate and Advanced Workshops

-  [Python Geospatial Fundamentals](https://github.com/dlab-berkeley/Geospatial-Data-and-Mapping-in-Python)
-  [Python Web Scraping and APIs](https://github.com/dlab-berkeley/Python-Web-Scraping)
-  [Python Machine Learning](https://github.com/dlab-berkeley/Python-Machine-Learning)
-  [Python Text Analysis](https://github.com/dlab-berkeley/Python-NLP-Fundamentals)
-  [Python Deep Learning](https://github.com/dlab-berkeley/Python-Deep-Learning)

# Contributors

-  [Mingyu Yuan](https://github.com/mingyu-yuan)
-  [Pratik Sachdeva](https://github.com/pssachdeva)
-  [Tom van Nuenen](https://github.com/tomvannuenen)
-  [Ben Gebre-Medhin](http://gebre-medhin.com)
-  [Laura Nelson](http://www.lauraknelson.com)
-  [Teddy Roland](https://teddyroland.com/about/)
-  [Geoff Bacon](http://linguistics.berkeley.edu/~bacon/)
-  [Caroline Le Pennec-Caldichoury](https://dlab.berkeley.edu/people/caroline-le-pennec)

These materials have evolved over a number of years. They were first developed
by Laura Nelson and Teddy Roland, with contributions and revisions made by Ben
Gebre-Medhin, Geoff Bacon, and Caroline Le Pennec-Caldichoury and Pratik Sachdeva. 
They were revamped by Mingyu Yuan in the summer of 2024.

