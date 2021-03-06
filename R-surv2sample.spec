%global packname  surv2sample
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Two-Sample Tests for Survival Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
The package provides tests for comparing two survival distributions,
testing equality of two cumulative incidence functions under competing
risks and checking goodness of fit of proportional rate models
(proportional hazards, proportional odds) for two samples.

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
%doc %{rlibdir}/surv2sample/html
%doc %{rlibdir}/surv2sample/DESCRIPTION
%{rlibdir}/surv2sample/R
%{rlibdir}/surv2sample/Meta
%{rlibdir}/surv2sample/INDEX
%{rlibdir}/surv2sample/data
RPM build errors:
%{rlibdir}/surv2sample/NAMESPACE
%{rlibdir}/surv2sample/libs
%{rlibdir}/surv2sample/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora