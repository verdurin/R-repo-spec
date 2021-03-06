%global packname  pspline
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.14
Release:          1%{?dist}
Summary:          Penalized Smoothing Splines

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-14.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-graphics 

BuildRequires:    R-devel tex(latex) R-stats R-graphics 

%description
Smoothing splines with penalties on order m derivatives.

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
%doc %{rlibdir}/pspline/html
%doc %{rlibdir}/pspline/DESCRIPTION
%{rlibdir}/pspline/INDEX
%{rlibdir}/pspline/NAMESPACE
%{rlibdir}/pspline/help
%{rlibdir}/pspline/R
%{rlibdir}/pspline/Meta
%{rlibdir}/pspline/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.14-1
- initial package for Fedora