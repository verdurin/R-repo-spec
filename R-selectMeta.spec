%global packname  selectMeta
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Estimation of weight functions in meta analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-DEoptim 

BuildRequires:    R-devel tex(latex) R-DEoptim 

%description
Publication bias, the fact that studies identified for inclusion in a meta
analysis do not represent all studies on the topic of interest, is
commonly recognized as a threat to the validity of the results of a meta
analysis. One way to explicitly model publication bias is via selection
models or weighted probability distributions. In this package we provide
implementations of several parametric and nonparametric weight functions.
The novelty in Rufibach (2011) is the proposal of a non-increasing variant
of the nonparametric weight function of Dear & Begg (1992). The new
approach potentially offers more insight in the selection process than
other methods, but is more flexible than parametric approaches. To
maximize the log-likelihood function proposed by Dear & Begg (1992) under
a monotonicity constraint we use a differential evolution algorithm
proposed by Ardia et al (2010a, b) and implemented in Mullen et al (2009).
In addition, we offer a method to compute a confidence interval for the
overall effect size theta, adjusted for selection bias as well as a
function that computes the simulation-based p-value to assess the null
hypothesis of no selection as described in Rufibach (2011, Section 6).

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
%doc %{rlibdir}/selectMeta/html
%doc %{rlibdir}/selectMeta/NEWS
%doc %{rlibdir}/selectMeta/DESCRIPTION
%{rlibdir}/selectMeta/data
%{rlibdir}/selectMeta/help
%{rlibdir}/selectMeta/R
%{rlibdir}/selectMeta/Meta
%{rlibdir}/selectMeta/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora