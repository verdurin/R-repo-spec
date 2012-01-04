%global packname  calmate
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7.0
Release:          1%{?dist}
Summary:          Post-calibration of allele-specific copy-number estimates (ASCNs)

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-R.methodsS3 R-R.oo R-R.utils R-matrixStats R-aroma.core 

BuildRequires:    R-devel tex(latex) R-MASS R-R.methodsS3 R-R.oo R-R.utils R-matrixStats R-aroma.core 

%description
Post-calibration of allele-specific copy-number estimates (ASCNs).

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.0-1
- initial package for Fedora