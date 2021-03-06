%global packname  MKLE
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.05
Release:          1%{?dist}
Summary:          Maximum kernel likelihood estimation.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Package for fast computation of the maximum kernel likelihood estimator

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
%doc %{rlibdir}/MKLE/html
%doc %{rlibdir}/MKLE/DESCRIPTION
%{rlibdir}/MKLE/R
%{rlibdir}/MKLE/data
%{rlibdir}/MKLE/INDEX
%{rlibdir}/MKLE/Meta
%{rlibdir}/MKLE/help
%{rlibdir}/MKLE/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.05-1
- initial package for Fedora