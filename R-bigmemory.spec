%global packname  bigmemory
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.2.11
Release:          1%{?dist}
Summary:          Manage massive matrices with shared memory and memory-mapped files

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils 

BuildRequires:    R-devel tex(latex) R-methods R-utils 

%description
Create, store, access, and manipulate massive matrices. Matrices are
allocated to shared memory and may use memory-mapped files.  Packages
biganalytics, bigtabulate, synchronicity, and bigalgebra provide advanced

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.2.11-1
- initial package for Fedora