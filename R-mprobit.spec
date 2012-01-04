%global packname  mprobit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.3
Release:          1%{?dist}
Summary:          Multivariate probit model for binary/ordinal response

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Multivariate normal rectangle probabilities (positive exchangeable,
general, approximations); MLE of regression and correlation parameters in
the multivariate binary/ordinal probit models: exchangeable, AR(1), and
unstructured correlation matrix.

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
%doc %{rlibdir}/mprobit/DESCRIPTION
%doc %{rlibdir}/mprobit/html
%{rlibdir}/mprobit/help
%{rlibdir}/mprobit/data
%{rlibdir}/mprobit/Meta
%{rlibdir}/mprobit/INDEX
%{rlibdir}/mprobit/R
%{rlibdir}/mprobit/libs
%{rlibdir}/mprobit/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.3-1
- initial package for Fedora