%global packname  AmpAffyExample
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.9
Release:          1%{?dist}
Summary:          Example of Amplified Data

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-affy 


BuildRequires:    R-devel tex(latex) R-affy



%description
Six arrays. Three from amplified RNA, three from the typical procedure.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.9-1
- initial package for Fedora