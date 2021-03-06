%global packname  PolynomF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.94
Release:          1%{?dist}
Summary:          Polynomials in R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Implements univariate polynomial operations in R

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
%doc %{rlibdir}/PolynomF/html
%doc %{rlibdir}/PolynomF/DESCRIPTION
%{rlibdir}/PolynomF/R
%{rlibdir}/PolynomF/libs
%{rlibdir}/PolynomF/Meta
%{rlibdir}/PolynomF/NAMESPACE
%{rlibdir}/PolynomF/help
%{rlibdir}/PolynomF/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.94-1
- initial package for Fedora