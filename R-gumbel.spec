%global packname  gumbel
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.03
Release:          1%{?dist}
Summary:          Gumbel copula

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
stand alone package providing R functions for the Gumbel-Hougaard copula.
We provide probality functions (cumulative distribution and density
functions), simulation function (Gumbel copula multivariate simulation)
and estimation functions (Maximum Likelihood Estimation, Inference For
Margins, Moment Based Estimation and Canonical Maximum Likelihood).

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
%doc %{rlibdir}/gumbel/DESCRIPTION
%doc %{rlibdir}/gumbel/html
%doc %{rlibdir}/gumbel/doc
%doc %{rlibdir}/gumbel/CITATION
%{rlibdir}/gumbel/INDEX
%{rlibdir}/gumbel/NAMESPACE
%{rlibdir}/gumbel/R
%{rlibdir}/gumbel/Meta
%{rlibdir}/gumbel/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.03-1
- initial package for Fedora