  Rope il_cut_l(Subsequence lb, Rope cut, Rope e, Subsequence rregion, Subsequence rb) {
    Rope res;
    append(res, '[');
    append(res, cut);
    append(res, e);
    append(res, ']');
    return res;
  }

  Rope il_cut_r(Subsequence lb, Subsequence lregion, Rope e, Rope cut, Subsequence rb) {
    Rope res;
    append(res, '[');
    append(res, e);
    append(res, cut);
    append(res, ']');
    return res;
  }
