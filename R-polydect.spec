%global packname  polydect
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          polydect

Group:            Applications/Engineering 
License:          X11
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
functions for one-dimension jump position detection using one-sided
polynomial kernel detectors (polynomial order from 0 to 3)

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
%doc %{rlibdir}/polydect/doc
%doc %{rlibdir}/polydect/DESCRIPTION
%doc %{rlibdir}/polydect/html
%{rlibdir}/polydect/data
%{rlibdir}/polydect/Meta
%{rlibdir}/polydect/R
%{rlibdir}/polydect/NAMESPACE
%{rlibdir}/polydect/help
%{rlibdir}/polydect/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora