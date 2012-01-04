%global packname  cmaes
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.11
Release:          1%{?dist}
Summary:          Covariance Matrix Adapting Evolutionary Strategy

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Single objective optimization using a CMA-ES.

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
%doc %{rlibdir}/cmaes/html
%doc %{rlibdir}/cmaes/DESCRIPTION
%{rlibdir}/cmaes/INDEX
%{rlibdir}/cmaes/help
%{rlibdir}/cmaes/NAMESPACE
%{rlibdir}/cmaes/R
%{rlibdir}/cmaes/Meta
%{rlibdir}/cmaes/unittests

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.11-1
- initial package for Fedora