%global packname  logging
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.92
Release:          1%{?dist}
Summary:          a tentative logging package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-92.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
a logging package emulating the python logging package.

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
%doc %{rlibdir}/logging/DESCRIPTION
%doc %{rlibdir}/logging/html
%{rlibdir}/logging/help
%{rlibdir}/logging/Meta
%{rlibdir}/logging/INDEX
%{rlibdir}/logging/R
%{rlibdir}/logging/unitTest
%{rlibdir}/logging/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.92-1
- initial package for Fedora