%global packname  dse2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2011.11.2
Release:          1%{?dist}
Summary:          DSE (unbundled transition package).

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2011.11-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-EvalEst 

BuildRequires:    R-devel tex(latex) R-EvalEst 

%description
This package is only to aid transition to the unbundled dse package. It
has no functions, but simply requires package EvalEst.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2011.11.2-1
- initial package for Fedora