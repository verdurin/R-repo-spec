%global packname  hapsim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Haplotype Data Simulation

Group:            Applications/Engineering 
License:          GPL version 2 or later
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Package for haplotype data simulation. Haplotypes are generated such that
their allele frequencies and linkage disequilibrium coefficients match
those estimated from an input data set.

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
%doc %{rlibdir}/hapsim/html
%doc %{rlibdir}/hapsim/DESCRIPTION
%{rlibdir}/hapsim/NAMESPACE
%{rlibdir}/hapsim/INDEX
%{rlibdir}/hapsim/Meta
%{rlibdir}/hapsim/R
%{rlibdir}/hapsim/help
%{rlibdir}/hapsim/libs
%{rlibdir}/hapsim/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora