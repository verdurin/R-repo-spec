%global packname  clustvarsel
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Variable Selection for Model-Based Clustering

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mclust 

BuildRequires:    R-devel tex(latex) R-mclust 

%description
The selection method uses either a greedy search or headlong search. The
greedy search at each step either checks all variables not currently
included in the set of clustering variables singly for inclusion into the
set or checks all variables in the set of clustering variables singly for
exclusion.The headlong search only checks until a variable is included or
excluded (i.e. does not necessarily check all possible variables for
inclusion/exclusion at each step) and any variable with evidence of
clustering below a certain level at any stage is removed from
consideration for the remainder of the algorithm. Each variable's evidence
for being useful to the clustering given the currently selected clustering
variables is given by the difference between the BIC for the model with
clustering (allowed to vary over 2 to a maximum number of groups and any
of the different covariance parameterizations allowed in mclust) using the
set of clustering variables including the variable being checked and the
sum of BICs for the model with clustering (allowed to vary over 2 to a
maximum number of groups and any of the different covariance
parameterizations allowed in mclust) using the set of clustering variables
without the variable being checked and the model for the variable being
checked being conditionally independent of the clustering given the other
clustering variables (this is modeled as a regression of the variable
being checked on the other clustering variables).

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora