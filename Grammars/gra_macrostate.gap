//This is the grammar, developed by Bjoern Voss, for the probablistic shape analysis of RNAshapes 2006 release. It is also known as "canonicals_nonamb" in the Haskell version of RNAshapes, or "adpf_nonamb"

//For better reading, we applied some renaming for the 2011 BMC Bioinformatics "Lost in folding space? Comparing four variants of the thermodynamic model for RNA secondary structure prediction" paper by S. Janssen et al.:
//  Terminal parsers:
//    b = BASE
//    loc = LOC
//    epsilon = EMPTY
//    r = REGION
//  Non-Terminals:
//    left_dg = left_dangle
//    noleft_dg = noleft_dangle
//    edgl = edanglel
//    edgr = edangler
//    edglr = edanglelr
//    nodg = nodangle
//    mc1 = ml_comps1
//    mc2 = ml_comps2
//    mc3 = ml_comps3
//    mc4 = ml_comps4
//    mcadd1 = no_dl_no_ss_end
//    mcadd2 = dl_or_ss_left_no_ss_end
//    mcadd3 = dl_or_ss_left_ss_end
//    mcadd4 = no_dl_ss_end
grammar gra_macrostate uses sig_foldrna(axiom = struct) {
	struct = left_dangle | trafo(noleft_dangle) | left_unpaired # h;

	left_unpaired = sadd(BASE, left_unpaired) | sadd(BASE, left_dangle) # h;

	left_dangle = ambd(edanglel, BASE, noleft_dangle) | cadd_Pr(edanglel, {noleft_dangle | nil(LOC)}) | cadd(edanglelr, {left_dangle | left_unpaired}) | nil(LOC) # h;

	noleft_dangle = cadd_Pr_Pr(edangler, {left_dangle | left_unpaired}) | cadd_Pr_Pr_Pr(nodangle, {noleft_dangle | nil(LOC)}) | ambd_Pr(nodangle, BASE, noleft_dangle) # h;

	edanglel = edl(BASE, closed, LOC) # h;

	edangler = edr(LOC, closed, BASE) # h;

	edanglelr = edlr(BASE, closed, BASE) # h;

	nodangle = drem(LOC, closed, LOC) # h;

	closed = stack | hairpin | multiloop | leftB | rightB | iloop # h;

	multiloop = {mldl(BASE, BASE, BASE, ml_comps1, BASE, BASE) | 
		mladl(BASE, BASE, BASE, ml_comps2, BASE, BASE) | 
		mldr(BASE, BASE, ml_comps3, BASE, BASE, BASE) | 
		mladr(BASE, BASE, ml_comps2, BASE, BASE, BASE) | 
		mldlr(BASE, BASE, BASE, ml_comps4, BASE, BASE, BASE) | 
		mladlr(BASE, BASE, BASE, ml_comps2, BASE, BASE, BASE) | 
		mldladr(BASE, BASE, BASE, ml_comps1, BASE, BASE, BASE) | 
		mladldr(BASE, BASE, BASE, ml_comps3, BASE, BASE, BASE)  | 
		ml(BASE, BASE, ml_comps2, BASE, BASE)} with stackpairing # h;

	ml_comps1 = combine(block_dl, no_dl_no_ss_end) | combine(block_dlr, dl_or_ss_left_no_ss_end) | acomb(block_dl, BASE, no_dl_no_ss_end) # h;

	ml_comps2 = combine(incl(nodangle), no_dl_no_ss_end) | combine(incl(edangler), dl_or_ss_left_no_ss_end) | acomb(incl(nodangle), BASE, no_dl_no_ss_end) # h;

	ml_comps3 = combine(incl(edangler), dl_or_ss_left_ss_end) | combine(incl(nodangle), no_dl_ss_end) | acomb(incl(nodangle), BASE, no_dl_ss_end) # h;

	ml_comps4 = combine(block_dl, no_dl_ss_end) | combine(block_dlr, dl_or_ss_left_ss_end) | acomb(block_dl, BASE, no_dl_ss_end) # h;

	block_dl = ssadd(REGION, edanglel) | incl(edanglel) # h;

	block_dlr = ssadd(REGION, edanglelr) | incl(edanglelr) # h;

	no_dl_no_ss_end = ml_comps2 | incl(nodangle) # h;

	dl_or_ss_left_no_ss_end = ml_comps1 | block_dl # h;

	no_dl_ss_end = ml_comps3 | incl(edangler) | addss(incl(edangler), REGION) # h;

	dl_or_ss_left_ss_end = ml_comps4 | block_dlr | addss(block_dlr, REGION) # h;

	stack = sr(BASE, closed, BASE) with basepairing # h;

	hairpin = hl(BASE, BASE, REGION with minsize(3), BASE, BASE) with stackpairing # h;

	leftB = bl(BASE, BASE, REGION, closed, BASE, BASE) with stackpairing # h;

	rightB = br(BASE, BASE, closed, REGION, BASE, BASE) with stackpairing # h;

	iloop = il(BASE, BASE, REGION with maxsize(30), closed, REGION with maxsize(30), BASE, BASE) with stackpairing # h;

}