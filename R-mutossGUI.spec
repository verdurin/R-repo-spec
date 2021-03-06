%global packname  mutossGUI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          A graphical user interface for the MuToss Project

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava R-JavaGD R-plotrix R-mutoss R-multcomp 

BuildRequires:    R-devel tex(latex) R-rJava R-JavaGD R-plotrix R-mutoss R-multcomp 

%description
A graphical user interface for the MuToss Project

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
%doc %{rlibdir}/mutossGUI/DESCRIPTION
%doc %{rlibdir}/mutossGUI/html
%{rlibdir}/mutossGUI/NAMESPACE
%{rlibdir}/mutossGUI/java-src
%{rlibdir}/mutossGUI/build.xml
%{rlibdir}/mutossGUI/java
%{rlibdir}/mutossGUI/Meta
%{rlibdir}/mutossGUI/R
%{rlibdir}/mutossGUI/INDEX
%{rlibdir}/mutossGUI/help

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora