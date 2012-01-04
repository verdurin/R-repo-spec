%global packname  hybridHclust
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Hybrid hierarchical clustering

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-cluster 

BuildRequires:    R-devel tex(latex) R-cluster 

%description
hybrid hierarchical clustering via mutual clusters

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
%doc %{rlibdir}/hybridHclust/html
%doc %{rlibdir}/hybridHclust/DESCRIPTION
%{rlibdir}/hybridHclust/Meta
%{rlibdir}/hybridHclust/data
%{rlibdir}/hybridHclust/R
%{rlibdir}/hybridHclust/demo
%{rlibdir}/hybridHclust/INDEX
%{rlibdir}/hybridHclust/NAMESPACE
%{rlibdir}/hybridHclust/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora