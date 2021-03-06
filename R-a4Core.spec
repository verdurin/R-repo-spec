%global packname  a4Core
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Automated Affymetrix Array Analysis Core Package

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-Biobase R-glmnet 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-glmnet 

%description
Automated Affymetrix Array Analysis Core Package

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
%doc %{rlibdir}/a4Core/NEWS
%doc %{rlibdir}/a4Core/html
%doc %{rlibdir}/a4Core/DESCRIPTION
%{rlibdir}/a4Core/NAMESPACE
%{rlibdir}/a4Core/R
%{rlibdir}/a4Core/Meta
%{rlibdir}/a4Core/INDEX
%{rlibdir}/a4Core/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora