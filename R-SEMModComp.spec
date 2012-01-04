%global packname  SEMModComp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Model Comparisons for SEM

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
Conduct tests of difference in fit for mean and covariance structure
models as in structural equation modeling (SEM)

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
%doc %{rlibdir}/SEMModComp/DESCRIPTION
%doc %{rlibdir}/SEMModComp/html
%{rlibdir}/SEMModComp/data
%{rlibdir}/SEMModComp/R
%{rlibdir}/SEMModComp/INDEX
%{rlibdir}/SEMModComp/help
%{rlibdir}/SEMModComp/Meta
%{rlibdir}/SEMModComp/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora