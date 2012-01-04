%global packname  gss
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.5
Release:          1%{?dist}
Summary:          General Smoothing Splines

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A comprehensive package for structural multivariate function estimation
using smoothing splines.

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
%doc %{rlibdir}/gss/html
%doc %{rlibdir}/gss/DESCRIPTION
%{rlibdir}/gss/NAMESPACE
%{rlibdir}/gss/INDEX
%{rlibdir}/gss/R
%{rlibdir}/gss/help
%{rlibdir}/gss/libs
%{rlibdir}/gss/data
%{rlibdir}/gss/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.5-1
- initial package for Fedora