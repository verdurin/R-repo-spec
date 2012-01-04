%global packname  SpatioTemporal
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Spatio-Temporal Model Estimation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Utilitis that estimate, predict and cross-validate the spatio-temporal
model developed for MESA Air.

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
%doc %{rlibdir}/SpatioTemporal/html
%doc %{rlibdir}/SpatioTemporal/DESCRIPTION
%doc %{rlibdir}/SpatioTemporal/doc
%{rlibdir}/SpatioTemporal/INDEX
%{rlibdir}/SpatioTemporal/data
%{rlibdir}/SpatioTemporal/R
%{rlibdir}/SpatioTemporal/help
%{rlibdir}/SpatioTemporal/NAMESPACE
%{rlibdir}/SpatioTemporal/libs
%{rlibdir}/SpatioTemporal/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.0-1
- initial package for Fedora