%global packname  recommenderlabJester
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Jester Dataset for recommenderlab

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-recommenderlab 

BuildRequires:    R-devel tex(latex) R-recommenderlab 

%description
Provides the Jester Dataset for recommenderlab

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
%doc %{rlibdir}/recommenderlabJester/DESCRIPTION
%doc %{rlibdir}/recommenderlabJester/html
%{rlibdir}/recommenderlabJester/Meta
%{rlibdir}/recommenderlabJester/INDEX
%{rlibdir}/recommenderlabJester/NAMESPACE
%{rlibdir}/recommenderlabJester/data
%{rlibdir}/recommenderlabJester/help

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora