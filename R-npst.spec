%global packname  npst
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Generalization of Hewitt's Seasonality Test

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Package 'npst' generalizes Hewitt's (1971) test for seasonality and
Rogerson's (1996) extension based on Monte-Carlo simulation.

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
%doc %{rlibdir}/npst/html
%doc %{rlibdir}/npst/DESCRIPTION
%{rlibdir}/npst/Meta
%{rlibdir}/npst/help
%{rlibdir}/npst/INDEX
%{rlibdir}/npst/R
%{rlibdir}/npst/libs
RPM build errors:
%{rlibdir}/npst/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora