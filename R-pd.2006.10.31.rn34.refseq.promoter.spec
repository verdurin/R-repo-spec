%global packname  pd.2006.10.31.rn34.refseq.promoter
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.99.0
Release:          1%{?dist}
Summary:          Platform Design Info for NimbleGen 2006-10-31_rn34_refseq_promoter

Group:            Applications/Engineering 
License:          LGPL (>= 2.0)
URL:              https://r-forge.r-project.org/projects/%{packname}/index.html
Source0:          https://r-forge.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-RSQLite R-oligoClasses R-DBI 
Requires:         R-Biostrings R-IRanges 

BuildRequires:    R-devel tex(latex) R-methods R-RSQLite R-oligoClasses R-DBI
BuildRequires:    R-Biostrings R-IRanges 


%description
Platform Design Info for NimbleGen 2006-10-31_rn34_refseq_promoter

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.0-1
- initial package for Fedora