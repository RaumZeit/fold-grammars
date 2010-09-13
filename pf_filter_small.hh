/* {{{

    This file is part of gapc (GAPC - Grammars, Algebras, Products - Compiler;
      a system to compile algebraic dynamic programming programs)

    Copyright (C) 2008  Georg Sauthoff
         email: gsauthof@techfak.uni-bielefeld.de or gsauthof@sdf.lonestar.org

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

}}} */

#ifndef PF_FILTER_HH
#define PF_FILTER_HH

/*
List_Ref<std::pair<Shape, pfanswer> > out::h(List_Ref<std::pair<Shape, pfanswer> > i_orig)
{
  std::pair<List<std::pair<Shape, pfanswer> >::iterator, List<std::pair<Shape, pfanswer> >::iterator> range = get_range(i_orig);
  List_Ref<std::pair<Shape, pfanswer> > i = h(range);
  return pf_filter(i);
 */


// avoid use of hashtable: because of filterering #classes is
// relatively small -> constant factor of hashtable is
// significant in this usecase


template <typename T>
struct p_func_filter
{

  static double cutoff_prob;

  double sum;
  p_func_filter()
    : sum(0) {}
  void update(const T &src)
  {
    sum += src.second;
  }
  bool ok(const T &x) const
  {
    double thresh = cutoff_prob  * sum;
    return x.second > thresh;
  }
};

template <typename T>
struct p_func_filter_all
{

  static double cutoff_prob;

  double sum;
  p_func_filter_all()
    : sum(0) {}
  void update(const T &src)
  {
    sum += src;
  }
  bool ok(const T &x) const
  {
    double thresh = cutoff_prob  * sum;
    return x > thresh;
  }
};

#ifdef GAPC_MOD_TRANSLATION_UNIT

template <typename T>
double p_func_filter<T>::cutoff_prob = 0.000001;

template <typename T>
double p_func_filter_all<T>::cutoff_prob = 0.000001;

#endif


#endif