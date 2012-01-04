%global packname  tlmec
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Linear Student-t Mixed-Effects Models with Censored Data

Group:            Applications/Engineering 
License:          GPL (>= 3.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
Fit a linear mixed effects model for censored data with Student-t or
normal distributions. The errors are assumed independent and identically

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
%doc %{rlibdir}/tlmec/html
%doc %{rlibdir}/tlmec/DESCRIPTION
%{rlibdir}/tlmec/INDEX
%{rlibdir}/tlmec/help
%{rlibdir}/tlmec/NAMESPACE
%{rlibdir}/tlmec/R
%{rlibdir}/tlmec/Meta
%{rlibdir}/tlmec/data

%changelog
* Mon Dec 05 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.1-1
- initial package for Fedora