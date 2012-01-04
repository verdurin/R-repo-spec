%global packname  aggrisk
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Estimate individual level risk using individual case data and spatially aggregated control data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package uses weighted estimating equations to estimate regression
parameters in the intensity function of an inhomogeneous spatial Poisson
process, when information on risk-factors is available at the individual
level for cases, but only at a spatially aggregated level for the
population at risk. Data-driven methods are used to select the weights
used in the estimating equations. A formal test is available to detect
non-Poisson behaviour in the underlying point process.

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
%doc %{rlibdir}/aggrisk/DESCRIPTION
%doc %{rlibdir}/aggrisk/html
%{rlibdir}/aggrisk/INDEX
%{rlibdir}/aggrisk/help
%{rlibdir}/aggrisk/Meta
%{rlibdir}/aggrisk/data
%{rlibdir}/aggrisk/R
%{rlibdir}/aggrisk/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora