%global packname  NISTnls
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.12
Release:          1%{?dist}
Summary:          Nonlinear least squares examples from NIST

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Datasets for testing nonlinear regression routines.

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
%doc %{rlibdir}/NISTnls/DESCRIPTION
%doc %{rlibdir}/NISTnls/html
%{rlibdir}/NISTnls/help
%{rlibdir}/NISTnls/NAMESPACE
%{rlibdir}/NISTnls/Meta
%{rlibdir}/NISTnls/R
%{rlibdir}/NISTnls/original
%{rlibdir}/NISTnls/data
%{rlibdir}/NISTnls/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.12-1
- initial package for Fedora