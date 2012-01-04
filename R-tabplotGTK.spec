%global packname  tabplotGTK
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          A graphical user interface for the tabplot package

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tabplot R-gWidgets R-gWidgetsRGtk2 R-classInt 


BuildRequires:    R-devel tex(latex) R-tabplot R-gWidgets R-gWidgetsRGtk2 R-classInt



%description
This package offers a GTK graphical user interface for the creation of
tableplots with the tabplot package.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.1-1
- initial package for Fedora