%global packname  DeducerPlugInScaling
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.7
Release:          1%{?dist}
Summary:          Reliability and factor analysis plugin

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Deducer R-psych R-GPArotation R-mvnormtest R-irr 

BuildRequires:    R-devel tex(latex) R-Deducer R-psych R-GPArotation R-mvnormtest R-irr 

%description
A Deducer plug-in for factor analysis and reliability analysis, using
psych, GPArotation and mvnormtest packages.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.7-1
- initial package for Fedora