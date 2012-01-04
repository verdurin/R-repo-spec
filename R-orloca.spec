%global packname  orloca
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.2
Release:          1%{?dist}
Summary:          The package deals with Operations Research LOCational Analysis models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
This version of the package deals with the min-sum ocation problem, also
known as Fermat--Weber problem or center location problem. The min-sum
location problem search for a point such that the weighted sum of the
distances to the demand points are minimized.

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
%doc %{rlibdir}/orloca/html
%doc %{rlibdir}/orloca/DESCRIPTION
%{rlibdir}/orloca/INDEX
%{rlibdir}/orloca/R
%{rlibdir}/orloca/NAMESPACE
%{rlibdir}/orloca/po
%{rlibdir}/orloca/demo
%{rlibdir}/orloca/Meta
%{rlibdir}/orloca/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.2-1
- initial package for Fedora