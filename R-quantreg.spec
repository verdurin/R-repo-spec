%global packname  quantreg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.76
Release:          1%{?dist}
Summary:          Quantile Regression

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-SparseM 


BuildRequires:    R-devel tex(latex) R-stats R-SparseM



%description
Quantile regression and related methods.

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
%doc %{rlibdir}/quantreg/html
%doc %{rlibdir}/quantreg/DESCRIPTION
%doc %{rlibdir}/quantreg/doc
%{rlibdir}/quantreg/Changelog
%{rlibdir}/quantreg/demo
%{rlibdir}/quantreg/NAMESPACE
%{rlibdir}/quantreg/help
%{rlibdir}/quantreg/LICENSE
%{rlibdir}/quantreg/INDEX
%{rlibdir}/quantreg/FAQ
%{rlibdir}/quantreg/data
%{rlibdir}/quantreg/libs
%{rlibdir}/quantreg/R
%{rlibdir}/quantreg/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.76-1
- initial package for Fedora