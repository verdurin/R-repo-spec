%global packname  lgcp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Log-Gaussian Cox Process

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-spatstat R-sp R-RandomFields R-iterators R-ncdf R-methods R-tcltk R-rgl R-rpanel R-fields R-rgdal R-maptools 


BuildRequires:    R-devel tex(latex) R-spatstat R-sp R-RandomFields R-iterators R-ncdf R-methods R-tcltk R-rgl R-rpanel R-fields R-rgdal R-maptools



%description
Spatial and spatio-temporal modelling of point patterns using the
log-Gaussian Cox process

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.0-1
- initial package for Fedora