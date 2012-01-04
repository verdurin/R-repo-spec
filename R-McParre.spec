%global packname  McParre
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Run a Regenerative Markov chain in Parallel on a Cluster

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
This package provides functions for a user to run a regenerative Markov
chain in parallel, split it up into tours and form Confidence Intervals on
parameters of interest.

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
%doc %{rlibdir}/McParre/html
%doc %{rlibdir}/McParre/DESCRIPTION
%{rlibdir}/McParre/runInteractiveParallel.R
%{rlibdir}/McParre/R
%{rlibdir}/McParre/RprofileINTERACTIVE
%{rlibdir}/McParre/help
%{rlibdir}/McParre/runBatchParallel.R
%{rlibdir}/McParre/INDEX
%{rlibdir}/McParre/RprofileBATCH
%{rlibdir}/McParre/libs
%{rlibdir}/McParre/demo
%{rlibdir}/McParre/runPetrolData.R
%{rlibdir}/McParre/NAMESPACE
%{rlibdir}/McParre/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora