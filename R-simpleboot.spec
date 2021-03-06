%global packname  simpleboot
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Simple Bootstrap Routines

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-boot 

BuildRequires:    R-devel tex(latex) R-boot 

%description
Simple bootstrap routines

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
%doc %{rlibdir}/simpleboot/DESCRIPTION
%doc %{rlibdir}/simpleboot/html
%doc %{rlibdir}/simpleboot/COPYING
%{rlibdir}/simpleboot/Meta
%{rlibdir}/simpleboot/INDEX
%{rlibdir}/simpleboot/help
%{rlibdir}/simpleboot/NAMESPACE
%{rlibdir}/simpleboot/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora