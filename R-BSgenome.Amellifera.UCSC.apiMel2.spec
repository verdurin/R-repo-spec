%global packname  BSgenome.Amellifera.UCSC.apiMel2
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.16
Release:          1%{?dist}
Summary:          Apis mellifera (Honey Bee) full genome (UCSC version apiMel2)

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-BSgenome 
Requires:         R-BSgenome 

BuildRequires:    R-devel tex(latex) R-BSgenome
BuildRequires:    R-BSgenome 


%description
Apis mellifera (Honey Bee) full genome as provided by UCSC (apiMel2, Jan.
2005) and stored in Biostrings objects.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.16-1
- initial package for Fedora