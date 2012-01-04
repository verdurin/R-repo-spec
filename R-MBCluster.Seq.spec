%global packname  MBCluster.Seq
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Model-Based Clustering for RNA-seq Data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Cluster genes based on Poisson or Negative-Binomial model for RNA-Seq or
other digital gene expression (DGE) data

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
%doc %{rlibdir}/MBCluster.Seq/html
%doc %{rlibdir}/MBCluster.Seq/DESCRIPTION
%{rlibdir}/MBCluster.Seq/data
%{rlibdir}/MBCluster.Seq/R
%{rlibdir}/MBCluster.Seq/Meta
%{rlibdir}/MBCluster.Seq/NAMESPACE
%{rlibdir}/MBCluster.Seq/INDEX
%{rlibdir}/MBCluster.Seq/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora