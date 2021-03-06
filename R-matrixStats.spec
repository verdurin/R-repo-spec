%global packname  matrixStats
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Methods that apply to rows and columns of a matrix

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-R.methodsS3 

BuildRequires:    R-devel tex(latex) R-methods R-R.methodsS3 

%description
This packages provides methods operating on rows and columns of matrices. 
The objective is to have all methods being optimized for speed and memory

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.0-1
- initial package for Fedora