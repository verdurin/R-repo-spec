%global packname  HumMeth27QCReport
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.11
Release:          1%{?dist}
Summary:          HumMeth27QCReport: quality control and preprocessing of Illumina's Infinium methylation assays.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methylumi R-lumi R-IlluminaHumanMethylation27k.db R-IlluminaHumanMethylation450k.db R-amap R-Hmisc R-gplots R-plotrix R-WriteXLS R-tcltk2 

BuildRequires:    R-devel tex(latex) R-methylumi R-lumi R-IlluminaHumanMethylation27k.db R-IlluminaHumanMethylation450k.db R-amap R-Hmisc R-gplots R-plotrix R-WriteXLS R-tcltk2 

%description
HumMeth27QCReport is a tool for quality control and preprocessing of
Illumina's Infinium BeadChip methylation assays. The automated analysis
pipeline comprises data import, normalization, quality diagnostics and
data export.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.11-1
- initial package for Fedora