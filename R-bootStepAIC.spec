%global packname  bootStepAIC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Bootstrap stepAIC

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Model selection by bootstrapping the stepAIC() procedure.

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
%doc %{rlibdir}/bootStepAIC/html
%doc %{rlibdir}/bootStepAIC/DESCRIPTION
%{rlibdir}/bootStepAIC/R
%{rlibdir}/bootStepAIC/help
%{rlibdir}/bootStepAIC/INDEX
%{rlibdir}/bootStepAIC/demo
%{rlibdir}/bootStepAIC/Meta
%{rlibdir}/bootStepAIC/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora