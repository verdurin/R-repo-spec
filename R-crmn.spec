%global packname  crmn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.14
Release:          1%{?dist}
Summary:          CCMN and other noRMalizatioN methods for metabolomics data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-pcaMethods R-Biobase R-pls R-methods 


BuildRequires:    R-devel tex(latex) R-pcaMethods R-Biobase R-pls R-methods



%description
Implements the Cross-contribution Compensating Multiple standard
Normalization (CCMN) method and other normalization algorithms.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.14-1
- initial package for Fedora