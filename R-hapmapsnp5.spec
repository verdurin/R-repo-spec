%global packname  hapmapsnp5
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.5
Release:          1%{?dist}
Summary:          Sample data - Hapmap SNP 5.0 Affymetrix

Group:            Applications/Engineering 
License:          GPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Sample dataset obtained from http://www.hapmap.org

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
%doc %{rlibdir}/hapmapsnp5/CITATION
%doc %{rlibdir}/hapmapsnp5/DESCRIPTION
%doc %{rlibdir}/hapmapsnp5/html
%{rlibdir}/hapmapsnp5/Meta
%{rlibdir}/hapmapsnp5/R
%{rlibdir}/hapmapsnp5/NAMESPACE
%{rlibdir}/hapmapsnp5/help
%{rlibdir}/hapmapsnp5/INDEX
%{rlibdir}/hapmapsnp5/celFiles

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.5-1
- initial package for Fedora