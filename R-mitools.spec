%global packname  mitools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Tools for multiple imputation of missing data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Tools to perform analyses and combine results from multiple-imputation

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
%doc %{rlibdir}/mitools/html
%doc %{rlibdir}/mitools/doc
%doc %{rlibdir}/mitools/NEWS
%doc %{rlibdir}/mitools/DESCRIPTION
%{rlibdir}/mitools/NAMESPACE
%{rlibdir}/mitools/Meta
%{rlibdir}/mitools/R
%{rlibdir}/mitools/dta
%{rlibdir}/mitools/demo
%{rlibdir}/mitools/data
%{rlibdir}/mitools/INDEX
%{rlibdir}/mitools/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.1-1
- initial package for Fedora