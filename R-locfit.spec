%global packname  locfit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.6
Release:          2%{?dist}
Summary:          Local Regression, Likelihood and Density Estimation.

Group:            Applications/Engineering 
License:          GPLv2+
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-akima R-lattice 

BuildRequires:    R-devel tex(latex) R-akima R-lattice 

%description
Local regression, likelihood and density estimation.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/libs

%changelog
* Mon Jan 30 2012 Adam Huffman <verdurin@fedoraproject.org> - 1.5.6-2
- fix files

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.6-1
- initial package for Fedora
