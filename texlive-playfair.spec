# revision 33193
# category Package
# catalog-ctan /fonts/playfair
# catalog-date 2014-03-16 11:38:42 +0100
# catalog-license ofl
# catalog-version undef
Name:		texlive-playfair
Version:	20140316
Release:	2
Summary:	Playfair Display fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/playfair
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/playfair.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/playfair.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Playfair Display is well suited for titling and headlines. It
has an extra large x-height and short descenders. It can be set
with no leading if space is tight, for instance in news
headlines, or for stylistic effect in titles. Capitals are
extra short, and only very slightly heavier than the lowercase
characters. This helps achieve a more even typographical colour
when typesetting proper nouns and initialisms.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_5ewtu2.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_6bqc7d.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_723q3k.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_aehru5.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_apfun2.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_c2cruh.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_cgf2ku.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_ev34te.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_ilriiw.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_j6ohis.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_ouuek2.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_qjvs44.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_rmgfzq.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_tcbmed.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_tff5oq.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_ujy7vm.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_vgw77z.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_vw64ij.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_ybdqh4.enc
%{_texmfdistdir}/fonts/enc/dvips/playfair/plf_zcb4ya.enc
%{_texmfdistdir}/fonts/map/dvips/playfair/PlayfairDisplay.map
%{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-Black.otf
%{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-BlackItalic.otf
%{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-Bold.otf
%{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-Italic.otf
%{_texmfdistdir}/fonts/opentype/public/playfair/PlayfairDisplay-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Black-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BlackItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/playfair/PlayfairDisplay-Regular-sup-t1.tfm
%{_texmfdistdir}/fonts/type1/public/playfair/PlayfairDisplay-Black.pfb
%{_texmfdistdir}/fonts/type1/public/playfair/PlayfairDisplay-BlackItalic.pfb
%{_texmfdistdir}/fonts/type1/public/playfair/PlayfairDisplay-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/playfair/PlayfairDisplay-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/playfair/PlayfairDisplay-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/playfair/PlayfairDisplay-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Black-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BlackItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/playfair/PlayfairDisplay-Regular-sup-t1.vf
%{_texmfdistdir}/tex/latex/playfair/LY1PlayfairDisplay-LF.fd
%{_texmfdistdir}/tex/latex/playfair/LY1PlayfairDisplay-OsF.fd
%{_texmfdistdir}/tex/latex/playfair/LY1PlayfairDisplay-Sup.fd
%{_texmfdistdir}/tex/latex/playfair/OT1PlayfairDisplay-LF.fd
%{_texmfdistdir}/tex/latex/playfair/OT1PlayfairDisplay-OsF.fd
%{_texmfdistdir}/tex/latex/playfair/OT1PlayfairDisplay-Sup.fd
%{_texmfdistdir}/tex/latex/playfair/PlayfairDisplay.sty
%{_texmfdistdir}/tex/latex/playfair/T1PlayfairDisplay-LF.fd
%{_texmfdistdir}/tex/latex/playfair/T1PlayfairDisplay-OsF.fd
%{_texmfdistdir}/tex/latex/playfair/T1PlayfairDisplay-Sup.fd
%{_texmfdistdir}/tex/latex/playfair/TS1PlayfairDisplay-LF.fd
%{_texmfdistdir}/tex/latex/playfair/TS1PlayfairDisplay-OsF.fd
%doc %{_texmfdistdir}/doc/fonts/playfair/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/playfair/Playfair_Display_A4_specimen.pdf
%doc %{_texmfdistdir}/doc/fonts/playfair/README
%doc %{_texmfdistdir}/doc/fonts/playfair/playfair-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/playfair/playfair-samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
