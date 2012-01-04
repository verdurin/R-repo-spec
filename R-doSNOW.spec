%global packname  doSNOW
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Foreach parallel adaptor for the snow package

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-foreach R-iterators R-snow R-utils 

BuildRequires:    R-devel tex(latex) R-foreach R-iterators R-snow R-utils 

%description
Provides a parallel backend for the %dopar% function using Luke Tierney's
snow package.

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
%doc %{rlibdir}/doSNOW/html
%doc %{rlibdir}/doSNOW/DESCRIPTION
%{rlibdir}/doSNOW/NAMESPACE
%{rlibdir}/doSNOW/R
%{rlibdir}/doSNOW/Meta
%{rlibdir}/doSNOW/help
%{rlibdir}/doSNOW/INDEX

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora