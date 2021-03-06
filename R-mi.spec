%global packname  mi
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.09.15
Release:          1%{?dist}
Summary:          Missing Data Imputation and Model Checking

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.09-15.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-MASS R-nnet R-car R-arm R-Matrix R-lme4 R-R2WinBUGS R-abind R-car 


BuildRequires:    R-devel tex(latex) R-methods R-MASS R-nnet R-car R-arm R-Matrix R-lme4 R-R2WinBUGS R-abind R-car



%description
Missing-data imputation and model checking

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.09.15-1
- initial package for Fedora