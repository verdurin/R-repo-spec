%global packname  munfold
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Metric Unfolding

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-memisc R-MASS 

BuildRequires:    R-devel tex(latex) R-memisc R-MASS 

%description
This package provides Schoenemans algorithm for metric multidimensional
unfolding and Procrustes rotation of unfolding results.

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
%doc %{rlibdir}/munfold/html
%doc %{rlibdir}/munfold/DESCRIPTION
%{rlibdir}/munfold/Meta
%{rlibdir}/munfold/NAMESPACE
%{rlibdir}/munfold/INDEX
%{rlibdir}/munfold/R
%{rlibdir}/munfold/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora