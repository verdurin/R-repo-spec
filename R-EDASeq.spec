%global packname  EDASeq
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Exploratory Data Analysis and Normalization for RNA-Seq

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-ShortRead R-Rsamtools R-aroma.light 

BuildRequires:    R-devel tex(latex) R-Biobase R-ShortRead R-Rsamtools R-aroma.light 

%description
Numerical and graphical summaries of RNA-Seq read data.  Within-lane
normalization procedures to adjust for GC-content effect (or other
gene-level effects) on read counts: loess robust local regression,
global-scaling, and full-quantile normalization (Risso et al., 2011).
Between-lane normalization procedures to adjust for distributional
differences between lanes (e.g., sequencing depth): global-scaling and
full-quantile normalization (Bullard et al., 2010).

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora