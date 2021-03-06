%global packname  PREDAsampledata
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          expression and copy number data on clear cell renal carcinoma samples

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-PREDA R-Biobase R-affy R-annotate R-gahgu133plus2.db R-gahgu133plus2cdf 

BuildRequires:    R-devel tex(latex) R-methods R-PREDA R-Biobase R-affy R-annotate R-gahgu133plus2.db R-gahgu133plus2cdf 

%description
Sample data for PREDA package. (annotations objects synchronized with
GeneAnnot custom CDFs version 2.2.0)

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.4-1
- initial package for Fedora