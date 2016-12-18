#Fold-Grammars : GAP Components
see also https://bibiserv.cebitec.uni-bielefeld.de/fold-grammars/ for the upstream description

##Description of the Bellman's GAP Repository: Fold-Grammars

Bellman's GAP is a domain specific language and compiler for dynamic programming over sequence data. It's name is derived from "Bellman's Principle of Optimality, Grammars, Algebras, and Products". A Bellman's GAP repository is an archive of re-usable modules. Repositories are provided for code sharing. If you have modules to share, write to Stefan Janssen sjanssen@techfak.uni-bielefeld.de

A typical program in Bellman's GAP contains four elements:

1. a signature, defining functions available in grammars which must be implemented in algebras,
2. one or more algebras, evaluating a candidate from the search space and applying the objective function,
3. one or more grammars, defining a search space of solution candidates
4. one or more executable program instances, combining a grammar with a product of algebras.

##Naming conventions

Although GAP-L (Bellman's GAP language) allows arbitrary names, i.e. they must match the regular expression [A-Z_a-z][A-Z_a-z0-9]*, for signatures, algebras and grammars, we restrict ourselves for a better reading to the following naming convention:
- signature names start with the prefix "sig_"
- algebra names start with the prefix "alg_"
- grammar names start with the prefix "gra_"
- for large elements, sub-fragments are outsourced in files starting with "XXXpart_"

We don't have a naming convention for instances, since they appear in a program just once. Names and file extensions for source code files can be chosen freely, but we prefer to use ".gap" for the file extension. Furthermore, if we split components of our program, we use the prefixes for the filenames as well.

##Repository content of Fold-Grammars

This repository is a collection of components (algebras, grammars, ...) for dynamic programming problems covering RNA secondary structure predictions. It covers the fields of:
- single structure prediction (similar to [RNAfold](http://www.tbi.univie.ac.at/RNA/documentation.html#rnafold)),
- prediction of structures for alignments (similar to [RNAalifold](http://www.tbi.univie.ac.at/RNA/documentation.html#rnaalifold)) [filenames with "ali_"],
- sequence structure evaluation (similar to [RNAeval](http://www.tbi.univie.ac.at/RNA/documentation.html#rnaeval)) [filenames with "eval_"] ,
- abstract shape analysis (similar the [RNAshapes](http://bibiserv.cebitec.uni-bielefeld.de/rnashapes/)) and HIshapes, and
- pseudoknot prediction (similar to [pknotsRG](http://bibiserv.cebitec.uni-bielefeld.de/pknotsrg/) and [pKiss](http://bibiserv.cebitec.uni-bielefeld.de/pkiss/)) [filenames with "pknot_"].
- outside computations, e.g. McCaskill base-pair probabilities, which also allow for Maximum Expected Accuracy (MEA) computations [filenames with "outside_"]

To capture different handling of dangling bases implemented in various programs, we provide the four different grammars (for details see [Lost in folding space? Comparing four variants of the thermodynamic model for RNA secondary structure prediction](http://www.biomedcentral.com/1471-2105/12/429/)). Compared to the supplementary file of that paper, we refined the grammars a little for more comfortable support of lonely base-pairs. This does not change their folding space. We also introduced filters for maximal loop length for bulges to be closer to the [ViennaRNA package](http://www.tbi.univie.ac.at/RNA), the only difference is, that the size of both unpaired regions of internal loops may not exceed 30 bases in Vienna RNA; we allow up to 30 bases on each side.)
- "nodangle" (no energy contributions of dangling bases at all),
- "overdangle" (available or not, bases next to a stem always dangle from both sides to this stem),
- "microstate" (by increasing the search space a lot, best of all four possibilities for dangling onto a stem is selected. OK for MFE computations, but wrong for probabilistic analyses) and
- "macrostate" (unambiguous handling of dangling bases, i.e. no search space inflation and dangling only available bases onto a stem. Violating Bellman's principle of optimality for MFE computations, but correct for probabilistic analyses by using a four component vector, instead of a single partition function value. This component trick is the reason for some special algebra versions for macrostate.)

##Repository structure

We massively use GAP-L's functionality of including source code fragments to maintain a clear structure of available components. Another advantage is the re-usability of components if they share the same signature.
