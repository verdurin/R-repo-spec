%global packname  genomatic
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.7
Release:          1%{?dist}
Summary:          Manages microsatellite projects.  Creates 96-well maps, genotyping submission forms, rerun management, and import into statistical software.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk 

BuildRequires:    R-devel tex(latex) R-tcltk 

%description
Manages DNA fragment analysis projects.  Creates 96-well maps, genotyping
submission forms, rerun management, and import to statistical software.

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
%doc %{rlibdir}/genomatic/html
%doc %{rlibdir}/genomatic/DESCRIPTION
%doc %{rlibdir}/genomatic/doc
%{rlibdir}/genomatic/NAMESPACE
%{rlibdir}/genomatic/INDEX
%{rlibdir}/genomatic/extdata
%{rlibdir}/genomatic/help
%{rlibdir}/genomatic/Meta
%{rlibdir}/genomatic/R
%{rlibdir}/genomatic/images

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.7-1
- initial package for Fedora