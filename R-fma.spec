%global packname  fma
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.00
Release:          1%{?dist}
Summary:          Data sets from "Forecasting: methods and applications" by Makridakis, Wheelwright & Hyndman (1998)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-stats R-tseries R-forecast 

BuildRequires:    R-devel tex(latex) R-graphics R-stats R-tseries R-forecast 

%description
All data sets from "Forecasting: methods and applications" by Makridakis,
Wheelwright & Hyndman (Wiley, 3rd ed., 1998).

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
%doc %{rlibdir}/fma/DESCRIPTION
%doc %{rlibdir}/fma/html
%{rlibdir}/fma/NAMESPACE
%{rlibdir}/fma/Meta
%{rlibdir}/fma/help
%{rlibdir}/fma/R
%{rlibdir}/fma/data
%{rlibdir}/fma/INDEX

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.00-1
- initial package for Fedora