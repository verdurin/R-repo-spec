%global packname  hypergraph
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          A package providing hypergraph data structures

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-graph 

BuildRequires:    R-devel tex(latex) R-methods R-graph 

%description
A package that implements some simple capabilities for representing and
manipulating hypergraphs.

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
%doc %{rlibdir}/hypergraph/html
%doc %{rlibdir}/hypergraph/DESCRIPTION
%{rlibdir}/hypergraph/NAMESPACE
%{rlibdir}/hypergraph/R
%{rlibdir}/hypergraph/Meta
%{rlibdir}/hypergraph/unitTests
%{rlibdir}/hypergraph/INDEX
%{rlibdir}/hypergraph/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora