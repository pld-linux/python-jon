%define	module	jonpy
Summary:	Jon's Python modules (jonpy)
Summary(pl):	Modu³y Pythona Jona (jonpy)
Name:		python-jon
Version:	0.06
Release:	2
License:	Custom
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	70974faf02353be0d3dc97c53a7e4ee4
URL:		http://jonpy.sourceforge.net/
Obsoletes:	jonpy
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These Python modules provide simple yet powerful multi-threaded
object-oriented CGI/FastCGI/mod_python/html-templating facilities for
the Python programming language.

%description -l pl
Te modu³y Pythona daj± proste, wielow±tkowe, zorientowane obiektowo
narzêdzia o du¿ych mo¿liwo¶ciach u³atwiaj±ce korzystanie z szablonów do
CGI, FastCGI, mod_pythona i HTML w jêzyku Python.

%package doc
Summary:	Documentation for Jon's Python modules
Summary(pl):	Dokumentacja do modu³ów Pythona Jona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This module contains documentation files for Jon's Python modules.

%description doc -l pl
Modu³ zawieraj±cy dokumentacjê dla modu³ów Pythona Jona.

%package examples
Summary:	Examples for Jon's Python modules
Summary(pl):	Przyk³adowe programy do modu³ów Pythona Jona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This module contains examples for Jon's Python modules.

%description examples -l pl
Modu³ zawieraj±cy przyk³adowe programy do modu³ów Pythona Jona.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version}}

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/jon{/wt,}/*.py

cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE README
%dir %{py_sitescriptdir}/jon
%{py_sitescriptdir}/jon/*.py[oc]
%dir %{py_sitescriptdir}/jon/wt
%{py_sitescriptdir}/jon/wt/*.py[oc]

%files doc
%defattr(644,root,root,755)
%doc doc/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
