%global packname  dressCheck
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          data and software for checking Dressman JCO 25(5) 2007

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase 

%description
data and software for checking Dressman JCO 25(5) 2007

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.4-1
- initial package for Fedora