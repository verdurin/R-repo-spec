%global packname  emplik2
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.10
Release:          1%{?dist}
Summary:          Empirical-likelihood test (two-sample, censored data)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Calculates the p-value for a mean-type hypothesis (or multiple mean-type
hypotheses) based on two samples.

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
%doc %{rlibdir}/emplik2/DESCRIPTION
%doc %{rlibdir}/emplik2/html
%{rlibdir}/emplik2/NAMESPACE
%{rlibdir}/emplik2/INDEX
%{rlibdir}/emplik2/Meta
%{rlibdir}/emplik2/help
%{rlibdir}/emplik2/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10-1
- initial package for Fedora