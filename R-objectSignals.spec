%global packname  objectSignals
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.10.2
Release:          1%{?dist}
Summary:          objectSignals

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
A mutable Signal object can report changes to its state, clients could
register functions so that they are called whenever the signal is emited.
The signal could be emited, disconnected, blocked, unblocked, and

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
%doc %{rlibdir}/objectSignals/NEWS
%doc %{rlibdir}/objectSignals/DESCRIPTION
%doc %{rlibdir}/objectSignals/html
%{rlibdir}/objectSignals/INDEX
%{rlibdir}/objectSignals/examples
%{rlibdir}/objectSignals/R
%{rlibdir}/objectSignals/NAMESPACE
%{rlibdir}/objectSignals/help
%{rlibdir}/objectSignals/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.10.2-1
- initial package for Fedora