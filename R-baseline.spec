%global packname  baseline
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Baseline Correction of Spectra

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 
Requires:         R-graphics R-SparseM 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-graphics R-SparseM 


%description
Collection of baseline correction algorithms, along with a framework and a
GUI for optimising baseline algorithm parameters.

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
%doc %{rlibdir}/baseline/html
%doc %{rlibdir}/baseline/DESCRIPTION
%{rlibdir}/baseline/NAMESPACE
%{rlibdir}/baseline/help
%{rlibdir}/baseline/INDEX
%{rlibdir}/baseline/Meta
%{rlibdir}/baseline/data
%{rlibdir}/baseline/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora