%global packname  lmomco
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.3
Release:          1%{?dist}
Summary:          L-moments, Censored L-moments, Trimmed L-moments, L-comoments, and Many Distributions

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
The package implements the statistical theory of L-moments in R including
L-moment estimation, probability-weighted moment estimation, parameter
estimation for numerous familiar and not-so-familiar distributions, and
L-moment estimation for the same distributions from the parameters.
L-moments are derived from the expectations of order statistics and are
linear with respect to the probability-weighted moments; choice of either
can be made by mathematical convenience. L-moments are directly analogous
to the well-known product moments; however, L-moments have many advantages
including unbiasedness, robustness, and consistency with respect to the
product moments. The method of L-moments can out perform the method of
maximum likelihood. The lmomco package historically is oriented around
canonical FORTRAN algorithms of J.R.M. Hosking, and the nomenclature for
many of the functions parallels that of the Hosking library, which later
became available in the lmom package. However, vast arrays of various
extensions and curiosities are added by the author to aid and expand the
breadth of L-moment application. Such extensions include venerable
statistics as Sen weighted mean, Gini mean difference, plotting positions,
and conditional probability adjustment. The plotting of L-moment ratio
diagrams is directly supported in this package. Computations of L-moments
for right-tail and left-tail censoring by known or unknown censoring
threshold and also by indicator variable also are available. E.A.H. Elamir
and A.H. Seheult have developed the trimmed L-moments, which are
implemented in this package, and numerical integration of quantile
functions is used to dynamically compute trajectories of select TL-moment
ratios for the construction of TL-moment ratio diagrams. Robert Serfling
and Peng Xiao have extended L-moments into multivariate space; the
so-called sample L-comoments are implemented here and might have
considerable application in copula theory because they measure asymmetric
correlation and higher co-moments. The supported distributions with moment
type shown as "L" (L-moments) or "TL" (trimmed L-moments) and additional
support for right-tail censoring ([RC]) include: Cauchy (TL), Exponential
(L), Gamma (L), Generalized Extreme Value (L), Generalized Lambda (L &
TL), Generalized Logistic (L), Generalized Normal (L), Generalized Pareto
(L[RC] & TL), Gumbel (L), Kappa (L), Kumaraswamy (L), Normal (L),
3-parameter log-Normal (L), Pearson Type III (L), Rayleigh (L), Reverse
Gumbel (L[RC]), Rice/Rician (L), Truncated Exponential (L), Wakeby (L),
and Weibull (L).

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
%doc %{rlibdir}/lmomco/html
%doc %{rlibdir}/lmomco/DESCRIPTION
%doc %{rlibdir}/lmomco/CITATION
%doc %{rlibdir}/lmomco/doc
%{rlibdir}/lmomco/testdata
%{rlibdir}/lmomco/READMEinst
%{rlibdir}/lmomco/data
%{rlibdir}/lmomco/WARRANTY
%{rlibdir}/lmomco/legacy
%{rlibdir}/lmomco/help
%{rlibdir}/lmomco/R
%{rlibdir}/lmomco/INDEX
%{rlibdir}/lmomco/Meta
%{rlibdir}/lmomco/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.3-1
- initial package for Fedora