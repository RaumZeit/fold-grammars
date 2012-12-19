#ifndef PKEXTRAS_HH
#define PKEXTRAS_HH

/* START: everything for strategy A: finding compatible pseudoknots */
	template<typename V, typename I>
	inline mfeanswer get_pk_fn(const Hash::Ref<V, I > &t) {
		//typename Hash::Ref<V, I > hash_h;
		Hash::Ref<V, I> &hash = const_cast<Hash::Ref<V, I>&>(t);
		mfeanswer a;
		typename Hash::Ref<V,I>::iterator i = hash.ref().begin();
		if (i == hash.ref().end()) {
			empty(a);
			return a;
		}
		a = (*i).second;
		++i;
		for (; i != hash.ref().end(); ++i) {
			mfeanswer b = (*i).second;
			if (b < a) {
				a = b;
			}
		}
		return a;
	}

	inline mfeanswer get_pk_fn(const mfeanswer &a) { 
		return a; 
	}

	template<typename B>
	inline mfeanswer &get_pk_fn(std::pair<mfeanswer, B> &p) { 
		return p.first; 
	}

	template<typename T, typename pos_int>
	inline mfeanswer get_pk_fn(List_Ref<T, pos_int> &l) {
		List<T, pos_int> &x = l.ref();
		mfeanswer a;
		typename List<T, pos_int>::iterator i = x.begin();
		if (i == x.end()) {
			empty(a);
			return a;
		}
		a = get_pk_fn(*i);
		++i;
		for (; i != x.end(); ++i) {
			mfeanswer t = get_pk_fn(*i);
			if (t < a) {
				a = t;
			}
		}
		return a;
	}

	#define get_pk(i, m) get_pk_fn( nt_help_pknot_free_kl(i, m) )
	#define get_pk_free_k(h, j, m, l) get_pk_fn( nt_help_pknot_free_k(h, j, m, l) )
	#define get_pk_free_l(i, m, h, l) get_pk_fn( nt_help_pknot_free_l(i, m, h, l) )
/* END: everything for strategy A: finding compatible pseudoknots */

	
//do a computation, but don't add computed candidates to the search space!
template<typename alphabet, typename pos_type, typename T>
inline bool ignore(const Basic_Sequence<alphabet, pos_type> &seq, T i, T j) {
  return false;
}


#ifdef GAPC_MOD_TRANSLATION_UNIT

/* START: everything for three dimensional tables in GAP, this is for strategy B */
	#include <utility>
	#include <limits>
	// Disable boost range checks: BOOST_DISABLE_ASSERTS
	#include <boost/multi_array.hpp>

	typedef boost::multi_array<std::pair<int, int>, 3> array_type;
	array_type::extent_gen extents;
	typedef boost::multi_array<bool, 3> tab_type;

	class ThreeD_private {
		private:
		protected:
			friend class ThreeD;
			bool init_;
			array_type array;
			tab_type tabulated;
			ThreeD_private() : init_(false) {
			}

			void init(size_t n) {
				if (init_) {
					return;
				}
				init_ = true;
				array.resize(extents[n][n][n]);
				tabulated.resize(extents[n][n][n]);
			}

			static const std::pair<int, int> inf;
	};
	const std::pair<int, int> ThreeD_private::inf = std::make_pair(std::numeric_limits<int>::max(), std::numeric_limits<int>::max());

	class ThreeD {
		private:
			ThreeD_private *d;
			ThreeD(const ThreeD &);
			ThreeD &operator=(const ThreeD &);
		
		public:
			ThreeD();
			~ThreeD();
			void set(int i, int j, int l, int k, int mfe, int n);
			const std::pair<int, int> &get(int i, int j, int l, int n);
	};

	ThreeD::ThreeD() {
	  d = new ThreeD_private();
	}

	ThreeD::~ThreeD() {
	  delete d;
	}

	void ThreeD::set(int i, int j, int l, int k, int mfe, int n) {
		array_type &array = d->array;
		tab_type &tabulated = d->tabulated;
		d->init(n+1);
		array[i][j][l] = std::make_pair(k, mfe);
		tabulated[i][j][l] = true;
	}

	const std::pair<int, int> &ThreeD::get(int i, int j, int l, int n) {
		array_type &array = d->array;
		tab_type &tabulated = d->tabulated;
		d->init(n+1);
		if (!tabulated[i][j][l]) {
			return d->inf;
		}
		return array[i][j][l];
	}

	ThreeD subopt_left, subopt_right, subopt_left_heuristic, subopt_right_heuristic;

	inline int get_energy(ThreeD &o, int i, int j, int l, int n) {
	  return o.get(i,j,l,n).second;
	}
	inline int get_index(ThreeD &o, int i, int j, int l, int n) {
	  return o.get(i,j,l,n).first;
	}
	inline void set(ThreeD &o, int i, int j, int l, int k, int mfe, int n) {
	  o.set(i,j,l,k,mfe,n);
	}
/* END: everything for three dimensional tables in GAP, this is for strategy B */


// helper function to get size of input. Needed in strategy B
template<typename alphabet, typename pos_type>
inline pos_type size(const Basic_Sequence<alphabet, pos_type> &seq) {
  return seq.size();
}


/* START: everything for strategy C */
	// storing <energy, index> for strategy C
	std::vector<std::pair<int, int> > rpk;

	inline void rpk_setup(int n) {
		rpk.resize(n);
		rpk[n-1] = std::make_pair(std::numeric_limits<int>::max(), 0);
	}

	inline int rpk_energy(int k) {
		assert(k<rpk.size());
		return rpk[k].first;
	}

	inline int rpk_index(int k) {
		assert(k<rpk.size());
		return rpk[k].second;
	}

	inline void rpk_set(int k) {
		assert(k+1<rpk.size());
		rpk[k] = rpk[k+1];
	}

	inline void rpk_set(int k, int e, int i) {
		assert(k<rpk.size());
		rpk[k] = std::make_pair(e, i);
	}
/* END: everything for strategy C */


#endif


#endif