%global packname  hsmm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.5.1
Release:          1%{?dist}
Summary:          Hidden Semi Markov Models

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-5.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A package for computation of hidden semi markov models

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
%doc %{rlibdir}/hsmm/html
%doc %{rlibdir}/hsmm/DESCRIPTION
%{rlibdir}/hsmm/demo
%{rlibdir}/hsmm/NAMESPACE
%{rlibdir}/hsmm/INDEX
%{rlibdir}/hsmm/help
%{rlibdir}/hsmm/Meta
%{rlibdir}/hsmm/libs
%{rlibdir}/hsmm/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.5.1-1
- initial package for Fedora