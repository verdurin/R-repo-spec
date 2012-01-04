%global packname  SuperLearner
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.4
Release:          1%{?dist}
Summary:          Super Learner Prediction

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-nnls R-quadprog 

BuildRequires:    R-devel tex(latex) R-nnls R-quadprog 

%description
This package implements the super learner prediction method and contains a
library of prediction algorithms to be used in the super learner.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.4-1
- initial package for Fedora