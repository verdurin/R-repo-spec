%global packname  R2Cuba
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Multidimensional Numerical Integration

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
R2Cuba implements four general-purpose multidimensional integration
algorithms: Vegas, Suave, Divonne and Cuhre

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
%doc %{rlibdir}/R2Cuba/html
%doc %{rlibdir}/R2Cuba/DESCRIPTION
%{rlibdir}/R2Cuba/libs
%{rlibdir}/R2Cuba/demo
RPM build errors:
%{rlibdir}/R2Cuba/Meta
%{rlibdir}/R2Cuba/help
%{rlibdir}/R2Cuba/R
%{rlibdir}/R2Cuba/INDEX
%{rlibdir}/R2Cuba/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora