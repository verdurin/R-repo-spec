%global packname  MVCClass
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          Model-View-Controller (MVC) Classes

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Creates classes used in model-view-controller (MVC) design

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
%doc %{rlibdir}/MVCClass/doc
%doc %{rlibdir}/MVCClass/DESCRIPTION
%doc %{rlibdir}/MVCClass/html
%{rlibdir}/MVCClass/INDEX
%{rlibdir}/MVCClass/R
%{rlibdir}/MVCClass/NAMESPACE
%{rlibdir}/MVCClass/Meta
%{rlibdir}/MVCClass/help
%{rlibdir}/MVCClass/paper

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.28.0-1
- initial package for Fedora