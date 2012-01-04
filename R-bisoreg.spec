%global packname  bisoreg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Bayesian Isotonic Regression with Bernstein Polynomials

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-bootstrap R-monreg R-R2WinBUGS R-coda 

BuildRequires:    R-devel tex(latex) R-bootstrap R-monreg R-R2WinBUGS R-coda 

%description
Bayesian monotonic regression function

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora