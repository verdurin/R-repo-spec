%global packname  xpose4
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.3.2
Release:          1%{?dist}
Summary:          Xpose 4

Group:            Applications/Engineering 
License:          LGPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-grid R-Hmisc R-gam R-methods R-xpose4data R-xpose4generic R-xpose4specific R-xpose4classic 

BuildRequires:    R-devel tex(latex) R-lattice R-grid R-Hmisc R-gam R-methods R-xpose4data R-xpose4generic R-xpose4specific R-xpose4classic 

%description
Xpose is collection of packages to be used as a model building aid for
non-linear mixed effects (population) analysis using NONMEM. It
facilitates data set checkout, exploration and visualization, model
diagnostics, candidate covariate identification and model comparison.
xpose4 is a package that links the other 4 packages together.

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
%doc %{rlibdir}/xpose4/DESCRIPTION
%doc %{rlibdir}/xpose4/html
%doc %{rlibdir}/xpose4/CITATION
%{rlibdir}/xpose4/readme.txt
%{rlibdir}/xpose4/Meta
%{rlibdir}/xpose4/changelog.txt
%{rlibdir}/xpose4/NAMESPACE
%{rlibdir}/xpose4/R
%{rlibdir}/xpose4/INDEX
%{rlibdir}/xpose4/xpose.ini
%{rlibdir}/xpose4/help

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.3.2-1
- initial package for Fedora