%global packname  compoisson
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Conway-Maxwell-Poisson Distribution

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-MASS 

BuildRequires:    R-devel tex(latex) R-stats R-MASS 

%description
Provides routines for density and moments of the Conway-Maxwell-Poisson
distribution as well as functions for fitting the COM-Poisson model for
over/under-dispersed count data.

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
%doc %{rlibdir}/compoisson/html
%doc %{rlibdir}/compoisson/DESCRIPTION
%{rlibdir}/compoisson/data
%{rlibdir}/compoisson/R
%{rlibdir}/compoisson/INDEX
%{rlibdir}/compoisson/help
%{rlibdir}/compoisson/NAMESPACE
%{rlibdir}/compoisson/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora