//this is the grammar Jens Reeder used as a base for in pknotsRG and in his early version of shape matchers

//For better reading, we applied some renaming for the 2011 BMC Bioinformatics "Lost in folding space? Comparing four variants of the thermodynamic model for RNA secondary structure prediction" paper by S. Janssen et al.:
//  Terminal parsers:
//    b = BASE
//    loc = LOC
//    epsilon = EMPTY
//    r = REGION
//  For consistency with MacroState nil has a LOC terminal parser instead of an EMPTY terminal parser.
grammar gra_overdangle_lp uses sig_foldrna(axiom = struct) {
  struct    = sadd(BASE, struct)   |
              cadd(dangle, struct) |
              nil(LOC)           # h;

  dangle    = drem(LOC, closed, LOC) # h;

  closed    = {stack                        | 
               hairpin                      |
               leftB                        | 
               rightB                       | 
               iloop                        | 
               multiloop} with basepairing # h;

  stack     = sr(BASE,                          closed,                          BASE) with basepairing # h;
  hairpin   = hl(BASE,                          REGION with minsize(3),          BASE) with basepairing # h;
  leftB     = bl(BASE, REGION,                  closed,                          BASE) with basepairing # h;
  rightB    = br(BASE,                          closed, REGION,                  BASE) with basepairing # h;
  iloop     = il(BASE, REGION with maxsize(30), closed, REGION with maxsize(30), BASE) with basepairing # h;
  multiloop = ml(BASE,                          ml_comps,                        BASE) with basepairing # h;

  ml_comps  = sadd(BASE, ml_comps)        |
              cadd(incl(dangle), ml_comps1) # h;

  ml_comps1 = sadd(BASE, ml_comps1)       |
              cadd(incl(dangle), ml_comps1) |
              incl(dangle)                  |
              addss(incl(dangle), REGION)   # h;
}