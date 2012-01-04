%global packname  interactivity
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          toggle R interactive mode.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Toggle R interactive mode by setting C level global variable

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
%doc %{rlibdir}/interactivity/html
%doc %{rlibdir}/interactivity/DESCRIPTION
%{rlibdir}/interactivity/INDEX
%{rlibdir}/interactivity/R
%{rlibdir}/interactivity/Meta
%{rlibdir}/interactivity/help
%{rlibdir}/interactivity/libs
%{rlibdir}/interactivity/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora