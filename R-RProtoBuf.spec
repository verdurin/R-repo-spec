%global packname  RProtoBuf
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          R Interface to the Protocol Buffers API

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RCurl R-Rcpp R-methods 


BuildRequires:    R-devel tex(latex) R-RCurl R-Rcpp R-methods



%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its
internal RPC protocols and file formats.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.3-1
- initial package for Fedora