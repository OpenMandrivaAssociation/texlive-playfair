Name:		texlive-playfair
Version:	64857
Release:	2
Summary:	Playfair Display fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/playfair
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/playfair.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/playfair.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/playfair
%{_texmfdistdir}/fonts/map/dvips/playfair
%{_texmfdistdir}/fonts/opentype/public/playfair
%{_texmfdistdir}/fonts/tfm/public/playfair
%{_texmfdistdir}/fonts/type1/public/playfair
%{_texmfdistdir}/fonts/vf/public/playfair
%{_texmfdistdir}/tex/latex/playfair
%doc %{_texmfdistdir}/doc/fonts/playfair

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
