%global packname  auteur
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.11.0612
Release:          1%{?dist}
Summary:          Bayesian sampler of the trait-evolutionary process

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ape R-geiger R-colorspace R-Rcpp 


BuildRequires:    R-devel tex(latex) R-ape R-geiger R-colorspace R-Rcpp



%description
Identifies shifts in process of continuous-trait evolution on phylogenetic

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.11.0612-1
- initial package for Fedora