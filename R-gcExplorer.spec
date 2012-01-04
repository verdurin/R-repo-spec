%global packname  gcExplorer
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.4
Release:          1%{?dist}
Summary:          Graphical Cluster Explorer

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-methods R-flexclust R-Rgraphviz 
Requires:         R-flexclust R-modeltools 

BuildRequires:    R-devel tex(latex) R-graphics R-methods R-flexclust R-Rgraphviz
BuildRequires:    R-flexclust R-modeltools 


%description
Visualize cluster results and investigate additional properties of
clusters using interactive neighbourhood graphs. By clicking on the node
representing the cluster, information about the cluster is provided using
additional graphics or summary statistics. For microarray data, tables
with links to genetic databases like NCBI Entrez Gene can be created for
each cluster.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.4-1
- initial package for Fedora