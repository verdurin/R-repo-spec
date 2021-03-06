%global packname  automap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.11
Release:          1%{?dist}
Summary:          Automatic interpolation package

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-sp R-gstat 
Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-methods R-sp R-gstat
BuildRequires:    R-lattice 


%description
This package performs an automatic interpolation by automatically
estimating the variogram and then calling gstat.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.11-1
- initial package for Fedora