%global packname  wvioplot
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Weighted violin plot

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Hmisc 

BuildRequires:    R-devel tex(latex) R-Hmisc 

%description
A violin plot is a combination of a box plot and a kernel density plot.

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
%doc %{rlibdir}/wvioplot/DESCRIPTION
%doc %{rlibdir}/wvioplot/html
%{rlibdir}/wvioplot/LICENSE
%{rlibdir}/wvioplot/help
%{rlibdir}/wvioplot/INDEX
%{rlibdir}/wvioplot/R
%{rlibdir}/wvioplot/NAMESPACE
%{rlibdir}/wvioplot/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora