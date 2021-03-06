%global packname  BiodiversityR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.6
Release:          1%{?dist}
Summary:          GUI for biodiversity and community ecology analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-vegan 


BuildRequires:    R-devel tex(latex) R-vegan



%description
This package provides a GUI (Graphical User Interface, via the
R-Commander) and some utility functions (often based on the vegan package)
for statistical analysis of biodiversity and ecological communities,
including species accumulation curves, diversity indices, Renyi profiles,
GLMs for analysis of species abundance and presence-absence, distance
matrices, Mantel tests, and cluster, constrained and unconstrained
ordination analysis. A book on biodiversity and community ecology analysis
is available for free download from the website.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6-1
- initial package for Fedora