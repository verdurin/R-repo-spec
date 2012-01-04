%global packname  benchden
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          28 benchmark densities from Berlinet/Devroye (1994)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Full implementation of the 28 distributions introduced as benchmarks for
nonparametric density estimation by Berlinet and Devroye (1994). Includes
densities, cdfs, quantile functions and generators for samples as well as
additional information on features of the densities. Also contains the 4
histogram densities used in Rozenholc/Mildenberger/Gather (2010).

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
%doc %{rlibdir}/benchden/html
%doc %{rlibdir}/benchden/DESCRIPTION
%{rlibdir}/benchden/R
%{rlibdir}/benchden/NAMESPACE
%{rlibdir}/benchden/help
%{rlibdir}/benchden/INDEX
%{rlibdir}/benchden/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora