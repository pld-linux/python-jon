%include	/usr/lib/rpm/macros.python
%define module jonpy
Summary:	Jon's Python modules (jonpy)
Summary(pl):	Modu³y Pythona Jona (jonpy)
Name:		python-jon
Version:	0.05
Release:	1
License:	Custom
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	269461eef986cc19a43c880580be5515
URL:		http://jonpy.sourceforge.net/
Obsoletes:	jonpy
BuildRequires:	rpm-pythonprov
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

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{py_sitedir}/jon{/wt,}/*.py

cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE README doc/*
%dir %{py_sitedir}/jon
%{py_sitedir}/jon/*.py?
%dir %{py_sitedir}/jon/wt
%{py_sitedir}/jon/wt/*.py?
%{_examplesdir}/*
