%global packname  eiPack
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          eiPack: Ecological Inference and Higher-Dimension Data Management

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-coda R-msm 

BuildRequires:    R-devel tex(latex) R-MASS R-coda R-msm 

%description
Provides methods for analyzing RxC ecological contingency tables using the
extreme case analysis, ecological regression, and Multinomial-Dirichlet
ecological inference models.  Also provides tools for manipulating
higher-dimension data objects.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.6-1
- initial package for Fedora