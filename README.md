# Innovized Progress (IP) Operators
This repository contains the working codes for the series of Innovized Progress Operators, including, IP2, IP3 and UIP operators. The details of these operators can be found in the book: https://link.springer.com/book/10.1007/978-981-99-2096-9
1. IP2 - Innovized Progress 2
2. IP3 - Innovized Progress 3
3. UIP - Unified Innovized Progress

# Contents
The MaOEAs included in this repository are:
1. NSGA-III, NSGA-III-IP2, NSGA-III-IP3 and NSGA-III-UIP
2. $\theta$-DEA, $\theta$-DEA-IP2, $\theta$-DEA-IP3 and $\theta$-DEA-UIP
3. MOEA/D, MOEA/D-IP2, MOEA/D-IP3 and MOEA/D-UIP

The relevant description, references and parameter settings, for the above MaOEAs can be found in book cited above. Notably, pymoo is a python-based platform used for developing MaOEAs. 

Further, the test problems used in the book include: (a) ZDT, (b) DTLZ, (c) MaF, (d) CIBN, (e) DAS-CMOP and (f) MF. pymoo does not cover all these test problems by default, owing to which, the source codes for the missing test problems have also been included in this repository.

# Requirements
For running the MaOEAs built on pymoo, make sure you have the following installed:
1. Python 3.6 or above: https://www.python.org/
2. pymoo package, as available on PyPi and can be installed using: pip install pymoo==0.4.2.2rc2
3. hvwfg package, as available on PyPi and can be installed using: pip install hvwfg

# Installation from this Repository
For MaOEAs built on pymoo:
1. download the respective file from “MaOEAs/pymoo” folder,
2. locate the “pymoo/algorithms” folder in your python installation directory, and
3. copy the downloaded file(s) in that folder.

# Instructions on how to run
For MaOEAs built on pymoo, a “.ipynb” notebook file has been provided in the “Run” folder. In that:
1. the problem name, and number of objectives (if applicable) need to be specified at the top, and
2. all cells are to be executed.

Notably, the “Problems/pymoo/maf.py” file should be copied to the current working directory.

If you have any difficulties running these codes, please write to dhish.saxena@me.iitr.ac.in or mittalsukrit@gmail.com

