%global packname  holdem
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Texas Holdem simulator

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Simulates hands and tournaments of Texas Holdem.

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
%doc %{rlibdir}/holdem/DESCRIPTION
%doc %{rlibdir}/holdem/html
%{rlibdir}/holdem/R
%{rlibdir}/holdem/INDEX
%{rlibdir}/holdem/Meta
%{rlibdir}/holdem/NAMESPACE
%{rlibdir}/holdem/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora