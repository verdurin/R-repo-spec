%global packname  nppbib
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Nonparametric Partially-Balanced Incomplete Block Design Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Implements a nonparametric statistical test for rank or score data from
partially-balanced incomplete block-design experiments.

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
%doc %{rlibdir}/nppbib/CITATION
%doc %{rlibdir}/nppbib/DESCRIPTION
%doc %{rlibdir}/nppbib/html
%{rlibdir}/nppbib/NAMESPACE
%{rlibdir}/nppbib/extdata
%{rlibdir}/nppbib/R
%{rlibdir}/nppbib/INDEX
%{rlibdir}/nppbib/help
%{rlibdir}/nppbib/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora