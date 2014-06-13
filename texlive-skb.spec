# revision 22781
# category Package
# catalog-ctan /macros/latex/contrib/skb
# catalog-date 2011-05-13 02:11:01 +0200
# catalog-license lppl1.3
# catalog-version 0.51
Name:		texlive-skb
Version:	0.51
Release:	7
Summary:	Tools for a repository of long-living documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/skb
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skb.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skb.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros that help to build a document
repository for long living documents. It focuses on structure
and re-use of text, code, figures etc. The basic concept is
first to separate structure from content (i.e., text about a
topic from the structure it is presented by) and then
separating the content from the actual published document, thus
enabling easy re-use of text blocks in different publications
(i.e., text about a protocol in a short article about this
protocol as well as in a book about many protocols); all
without constantly copying or changing text. As a side effect,
using the document classes provided, it hides a lot of LaTeX
from someone who just wants to write articles and books.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/skb/skb.cfg
%{_texmfdistdir}/tex/latex/skb/skb.sty
%{_texmfdistdir}/tex/latex/skb/skbarticle.cls
%{_texmfdistdir}/tex/latex/skb/skbbeamer.cls
%{_texmfdistdir}/tex/latex/skb/skbbook.cls
%{_texmfdistdir}/tex/latex/skb/skblncsbeamer.cls
%{_texmfdistdir}/tex/latex/skb/skblncsppt.cls
%{_texmfdistdir}/tex/latex/skb/skbmoderncv.cls
%doc %{_texmfdistdir}/doc/latex/skb/HISTORY.TXT
%doc %{_texmfdistdir}/doc/latex/skb/LICENSE.TXT
%doc %{_texmfdistdir}/doc/latex/skb/MANIFEST.TXT
%doc %{_texmfdistdir}/doc/latex/skb/README
%doc %{_texmfdistdir}/doc/latex/skb/TODO.TXT
%doc %{_texmfdistdir}/doc/latex/skb/makefile
%doc %{_texmfdistdir}/doc/latex/skb/skb.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/acronyms.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibliography.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex-styles.bbx
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/article.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/book.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/collection.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/conference.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/inbook.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/incollection.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/inproceedings.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/manual.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/misc.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/online.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/proceedings.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/report.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/standard.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/techreport.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/database/bibtex/unpublished.bib
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/example-toc.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/example.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/figure-classic.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/listings.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/optional-text.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/paths.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/rebuild.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/skbconfig.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/skbem.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/skbfigure.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/skbheading.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/skbinput.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/skbslide.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/skbslidecite.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/examples/used-options.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/dirtree/baf.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/dirtree/complete.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/dirtree/exa-doc.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/dirtree/publish-art.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/dirtree/publish.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/dirtree/repository.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/dirtree/skb-distribution.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-0.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-1.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-10.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-11.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-12.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-13.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-14.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-2.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-3.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-4.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-5.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-6.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-7.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-8.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/figures/multiexample/dpe-9.pdf
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/abstract.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/applicability.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/exa-doc/documentation.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/example-article.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/getting-started/config-cmd.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/getting-started/config-opt-table.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/getting-started/config-opt.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/getting-started/config.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/getting-started/distribution.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/getting-started/folders.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/getting-started/installation.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/getting-started/rebuild.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/getting-started/start.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/getting-started/used-options.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/intent.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/acr-bib.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/figures.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/figures2.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/headings-and-files.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/listing.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/lists.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/manual.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/optional-text.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/path-commands.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/pdfinfo.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/skbem.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/skbfigure-opt-table.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/skbinput-opt-table.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/slides.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/manual/slides2.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/separate/separate-cs.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/separate/separate-final.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/separate/separate-parts-baf.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/separate/separate-parts-pc.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/separate/separate-parts-pc2.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/separate/separate-parts.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/separate/separate.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/story/long.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/story/long2.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/story/short.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/repository/title.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/about.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/applicability.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/example-art-tex1.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/example-art-tex2.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/example-art-tex3.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/example-art-toc.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/intent.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-acrbib.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-figures-exa.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-figures-exna.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-figures-opt.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-figures.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-haf.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-listings.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-lists.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-optional-text.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-paths.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-pdfinfo.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-skbem.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-slides1.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/manual-slides2.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/separate-cs.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/separate-parts-baf.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/separate-parts-pc1.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/separate-parts-pc2.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/separate.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/start-config-cmd.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/start-config-opt.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/start-distribution.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/start-folders.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/start-installation.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/start-rebuild1.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/start-rebuild2.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/start-used-options.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/story-long1.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/story-long2.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/slides/story-short.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/ug-slides-anim.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/ug-slides-load.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/ug-slides-noanim.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/ug-slides-notes.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/user-guide-load.tex
%doc %{_texmfdistdir}/doc/latex/skb/user-guide/user-guide.tex
#- source
%doc %{_texmfdistdir}/source/latex/skb/skb.dtx
%doc %{_texmfdistdir}/source/latex/skb/skb.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.51-2
+ Revision: 756064
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.51-1
+ Revision: 719546
- texlive-skb
- texlive-skb
- texlive-skb
- texlive-skb

