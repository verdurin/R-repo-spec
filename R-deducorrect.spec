%global packname  deducorrect
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Deductive correction of simple rounding, typing and sign errors

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-editrules 

BuildRequires:    R-devel tex(latex) R-editrules 

%description
Deductive correction of simple rounding, typing and sign errors

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
%doc %{rlibdir}/deducorrect/doc
%doc %{rlibdir}/deducorrect/html
%doc %{rlibdir}/deducorrect/DESCRIPTION
%doc %{rlibdir}/deducorrect/NEWS
%{rlibdir}/deducorrect/NAMESPACE
%{rlibdir}/deducorrect/help
%{rlibdir}/deducorrect/INDEX
%{rlibdir}/deducorrect/tests
%{rlibdir}/deducorrect/R
%{rlibdir}/deducorrect/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora