%global packname  ITALICS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.14.0
Release:          1%{?dist}
Summary:          ITALICS

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-GLAD R-ITALICSData R-oligo R-affxparser R-pd.mapping50k.xba240 

BuildRequires:    R-devel tex(latex) R-GLAD R-ITALICSData R-oligo R-affxparser R-pd.mapping50k.xba240 

%description
A Method to normalize of Affymetrix GeneChip Human Mapping 100K and 500K

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.14.0-1
- initial package for Fedora