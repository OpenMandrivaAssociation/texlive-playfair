%global tl_name playfair
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Playfair Display fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/playfair
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/playfair.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/playfair.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the PlayFairDisplay family of fonts, designed by
Claus Eggers Sorensen, for use with LaTeX, pdfLaTeX, XeLaTeX and
LuaLaTeX. PlayFairDisplay is well suited for titling and headlines. It
has an extra large x-height and short descenders. It can be set with no
leading if space is tight, for instance in news headlines, or for
stylistic effect in titles. Capitals are extra short, and only very
slightly heavier than the lowercase characters. This helps achieve a
more even typographical colour when typesetting proper nouns and
initialisms.

