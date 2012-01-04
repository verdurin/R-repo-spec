%global packname  mfp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.9
Release:          1%{?dist}
Summary:          Multivariable Fractional Polynomials

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Fractional polynomials are used to represent curvature in regression
models. A key reference is Royston and Altman, 1994.

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
%doc %{rlibdir}/mfp/html
%doc %{rlibdir}/mfp/doc
%doc %{rlibdir}/mfp/DESCRIPTION
%{rlibdir}/mfp/R
%{rlibdir}/mfp/Meta
%{rlibdir}/mfp/NAMESPACE
%{rlibdir}/mfp/help
%{rlibdir}/mfp/data
%{rlibdir}/mfp/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.9-1
- initial package for Fedora