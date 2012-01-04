%global packname  spa
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Implements The Sequential Predictions Algorithm

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-cluster R-MASS 

BuildRequires:    R-devel tex(latex) R-cluster R-MASS 

%description
Implements the Sequential Predictions Algorithm

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
%doc %{rlibdir}/spa/DESCRIPTION
%doc %{rlibdir}/spa/CITATION
%doc %{rlibdir}/spa/html
%{rlibdir}/spa/R
%{rlibdir}/spa/help
%{rlibdir}/spa/INDEX
%{rlibdir}/spa/data
%{rlibdir}/spa/NAMESPACE
%{rlibdir}/spa/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora