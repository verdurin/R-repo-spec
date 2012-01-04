%global packname  spikeslab
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Prediction and variable selection using spike and slab regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lars R-randomForest 

BuildRequires:    R-devel tex(latex) R-lars R-randomForest 

%description
Spike and slab for prediction and variable selection in linear regression
models. Uses a generalized elastic net for variable selection.

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
%doc %{rlibdir}/spikeslab/CITATION
%doc %{rlibdir}/spikeslab/html
%doc %{rlibdir}/spikeslab/DESCRIPTION
%doc %{rlibdir}/spikeslab/NEWS
%doc %{rlibdir}/spikeslab/doc
%{rlibdir}/spikeslab/libs
%{rlibdir}/spikeslab/data
%{rlibdir}/spikeslab/R
%{rlibdir}/spikeslab/help
%{rlibdir}/spikeslab/LICENSE
%{rlibdir}/spikeslab/Meta
%{rlibdir}/spikeslab/NAMESPACE
%{rlibdir}/spikeslab/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.4-1
- initial package for Fedora