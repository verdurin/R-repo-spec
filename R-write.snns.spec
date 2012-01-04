%global packname  write.snns
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.4.2
Release:          1%{?dist}
Summary:          Function for exporting data to SNNS pattern files.

Group:            Applications/Engineering 
License:          GPL ( version 2 or later)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-4.2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Function for writing a SNNS pattern file from a data.frame or matrix.

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
%doc %{rlibdir}/write.snns/html
%doc %{rlibdir}/write.snns/DESCRIPTION
%{rlibdir}/write.snns/NAMESPACE
%{rlibdir}/write.snns/help
%{rlibdir}/write.snns/R
%{rlibdir}/write.snns/Meta
%{rlibdir}/write.snns/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.4.2-1
- initial package for Fedora