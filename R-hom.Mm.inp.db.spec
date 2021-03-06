%global packname  hom.Mm.inp.db
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.6.1
Release:          1%{?dist}
Summary:          Homology information for Mus musculus from Inparanoid

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-AnnotationDbi 
Requires:         R-methods R-AnnotationDbi 

BuildRequires:    R-devel tex(latex) R-methods R-AnnotationDbi
BuildRequires:    R-methods R-AnnotationDbi 


%description
Homology information for Mus musculus from Inparanoid assembled using data
from public repositories

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6.1-1
- initial package for Fedora