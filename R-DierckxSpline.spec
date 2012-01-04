%global packname  DierckxSpline
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          R companion to "Curve and Surface Fitting with Splines"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-lattice R-PolynomF 

BuildRequires:    R-devel tex(latex) R-stats R-lattice R-PolynomF 

%description
This package provides a wrapper to the FITPACK routines written by Paul
Dierckx. The original Fortran is available from

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
%doc %{rlibdir}/DierckxSpline/html
%doc %{rlibdir}/DierckxSpline/DESCRIPTION
%{rlibdir}/DierckxSpline/scripts
%{rlibdir}/DierckxSpline/jsm2007
%{rlibdir}/DierckxSpline/INDEX
%{rlibdir}/DierckxSpline/help
%{rlibdir}/DierckxSpline/libs
%{rlibdir}/DierckxSpline/data
%{rlibdir}/DierckxSpline/NAMESPACE
%{rlibdir}/DierckxSpline/R
%{rlibdir}/DierckxSpline/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.4-1
- initial package for Fedora