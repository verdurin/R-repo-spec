%global packname  RpsiXML
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.0
Release:          1%{?dist}
Summary:          R interface to PSI-MI 2.5 files

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-annotate R-graph R-Biobase R-RBGL R-XML R-hypergraph R-AnnotationDbi 


BuildRequires:    R-devel tex(latex) R-methods R-annotate R-graph R-Biobase R-RBGL R-XML R-hypergraph R-AnnotationDbi



%description
Queries, data structure and interface to visualization of interaction
datasets. This package inplements the PSI-MI 2.5 standard and supports up
to now 8 databases. Further databases supporting PSI-MI 2.5 standard will
be added continuously.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.0-1
- initial package for Fedora