%global packname  beadarray
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4.1
Release:          1%{?dist}
Summary:          Quality assessment and low-level analysis for Illumina BeadArray data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-methods R-ggplot2 

BuildRequires:    R-devel tex(latex) R-Biobase R-methods R-ggplot2 

%description
The package is able to read bead-level data (raw TIFFs and text files)
output by BeadScan as well as bead-summary data from BeadStudio.  Methods
for quality assessment and low-level analysis are provided.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.1-1
- initial package for Fedora