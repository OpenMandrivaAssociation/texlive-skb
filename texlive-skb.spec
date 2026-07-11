%global tl_name skb
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.52
Release:	%{tl_revision}.1
Summary:	Tools for a repository of long-living documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/skb
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skb.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skb.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros that help to build a document repository for
long living documents. It focuses on structure and re-use of text, code,
figures etc. The basic concept is first to separate structure from
content (i.e., text about a topic from the structure it is presented by)
and then separating the content from the actual published document, thus
enabling easy re-use of text blocks in different publications (i.e.,
text about a protocol in a short article about this protocol as well as
in a book about many protocols); all without constantly copying or
changing text. As a side effect, using the document classes provided, it
hides a lot of LaTeX from someone who just wants to write articles and
books.

