%global packname  pgirmess
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5.2
Release:          1%{?dist}
Summary:          Data analysis in ecology

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Description: Miscellaneous functions for analysis and display of
ecological and spatial data

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
%doc %{rlibdir}/pgirmess/DESCRIPTION
%doc %{rlibdir}/pgirmess/html
%{rlibdir}/pgirmess/data
%{rlibdir}/pgirmess/Meta
%{rlibdir}/pgirmess/R
%{rlibdir}/pgirmess/NAMESPACE
%{rlibdir}/pgirmess/help
%{rlibdir}/pgirmess/INDEX

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.2-1
- initial package for Fedora