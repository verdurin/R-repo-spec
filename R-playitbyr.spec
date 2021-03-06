%global packname  playitbyr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Representing and exploring data through sound

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-audio 

BuildRequires:    R-devel tex(latex) R-audio 

%description
playitbyr is a flexible toolkit for data analysis and exploration in R.
The functions allow the user to map data onto sonic parameters like pitch,
tempo, and rhythm, and output sound and sound files.

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
%doc %{rlibdir}/playitbyr/DESCRIPTION
%doc %{rlibdir}/playitbyr/html
%{rlibdir}/playitbyr/R
%{rlibdir}/playitbyr/INDEX
%{rlibdir}/playitbyr/Meta
%{rlibdir}/playitbyr/NAMESPACE
%{rlibdir}/playitbyr/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora