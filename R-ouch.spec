%global packname  ouch
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.8.1
Release:          1%{?dist}
Summary:          Ornstein-Uhlenbeck models for phylogenetic comparative hypotheses

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats R-graphics R-subplex 

BuildRequires:    R-devel tex(latex) R-methods R-stats R-graphics R-subplex 

%description
Fit and compare Ornstein-Uhlenbeck models for evolution along a
phylogenetic tree.

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
%doc %{rlibdir}/ouch/DESCRIPTION
%doc %{rlibdir}/ouch/html
%doc %{rlibdir}/ouch/CITATION
%doc %{rlibdir}/ouch/NEWS
%{rlibdir}/ouch/ChangeLog
%{rlibdir}/ouch/NAMESPACE
%{rlibdir}/ouch/GPL
%{rlibdir}/ouch/INDEX
%{rlibdir}/ouch/help
%{rlibdir}/ouch/Meta
%{rlibdir}/ouch/data
%{rlibdir}/ouch/LICENSE
%{rlibdir}/ouch/libs
%{rlibdir}/ouch/OCHANGELOG
%{rlibdir}/ouch/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.8.1-1
- initial package for Fedora