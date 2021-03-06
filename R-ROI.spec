%global packname  ROI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.6
Release:          1%{?dist}
Summary:          R Optimization Infrastructure

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-methods R-registry R-slam 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-methods R-registry R-slam 


%description
The R Optimization Infrastructure (ROI) package provides a sophisticated
framework for handling optimization problems in R.

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
%doc %{rlibdir}/ROI/html
%doc %{rlibdir}/ROI/DESCRIPTION
%{rlibdir}/ROI/R
%{rlibdir}/ROI/NAMESPACE
%{rlibdir}/ROI/help
%{rlibdir}/ROI/INDEX
%{rlibdir}/ROI/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.6-1
- initial package for Fedora