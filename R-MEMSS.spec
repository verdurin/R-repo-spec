%global packname  MEMSS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Data sets from Mixed-effects Models in S

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lme4 


BuildRequires:    R-devel tex(latex) R-lme4



%description
Data sets and sample analyses from Pinheiro and Bates, "Mixed-effects
Models in S and S-PLUS" (Springer, 2000).

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
%doc %{rlibdir}/MEMSS/DESCRIPTION
%doc %{rlibdir}/MEMSS/html
%{rlibdir}/MEMSS/INDEX
%{rlibdir}/MEMSS/Meta
%{rlibdir}/MEMSS/help
%{rlibdir}/MEMSS/data
%{rlibdir}/MEMSS/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.0-1
- initial package for Fedora