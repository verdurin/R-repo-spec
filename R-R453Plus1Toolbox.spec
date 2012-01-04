%global packname  R453Plus1Toolbox
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          A package for importing and analyzing data from Roche's Genome Sequencer System.

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-Biostrings R-BSgenome.Scerevisiae.UCSC.sacCer2 

BuildRequires:    R-devel tex(latex) R-Biobase R-Biostrings R-BSgenome.Scerevisiae.UCSC.sacCer2 

%description
The R453Plus1 Toolbox comprises useful functions for the analysis of data
generated by Roche's 454 sequencing platform. It adds functions for
quality assurance as well as for annotation and visualization of detected
variants, complementing the software tools shipped by Roche with their
product. Further, a pipeline for the detection of structural variants is

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora