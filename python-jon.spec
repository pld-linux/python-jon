%include	/usr/lib/rpm/macros.python
%define module jonpy
Summary:	Jon's Python modules (jonpy)
Summary(pl):	Modu³y Pythona Jona (jonpy)
Name:		python-jon
Version:	0.03
Release:	0.1
License:	Custom
Group:		Libraries/Python
Source0:	http://prdownloads.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
URL:		http://jonpy.sourceforge.net/
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These Python modules provide simple yet powerful multi-threaded
object-oriented CGI/FastCGI/mod_python/html-templating facilities for
the Python programming language.

%description -l pl
Te modu³y Pythona daj± proste, wielow±tkowe, zorientowane obiektowo
narzêdzia o du¿ych mo¿liwo¶ciach u³atwiaj±ce korzystanie z szablonów do
CGI, FastCGI, mod_pythona i HTML w jêzyku Python.

%package cgi
Summary:	Abstraction layer for CGI-style applications
Summary(pl):	Abstrakcyjna warstwa dla aplikacji w stylu CGI
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description cgi
The jon-cgi module provides an object-oriented interface for writing
CGI and CGI-style programs. It provides an abstraction layer so that
the same code can be used with either standard CGI or replacement
technologies such as FastCGI.

%description cgi -l pl
Modu³ jon-cgi daje zorientowany obiektowo interfejs do pisania programów
CGI oraz w stylu CGI. Zapewnia abstrakcjyjn± warstwê pozwalaj±c na u¿ycie
tego samego kodu w zwyk³ym CGI jak i zamiennych technologiach, jak FastCGI.

%package modpy
Summary:	A connector to use the abstraction layer with mod_python
Summary(pl):	£±cznik pomiêdzy warstw± abstrakcyjn± a modu³em mod_python
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description modpy
The jon-modpy module builds upon the classes defined in the cgi module
to allow code originally written with the CGI protocol in mind to be
used unchanged with the mod_python module.

%description modpy -l pl
Modu³ jon-modpy jest zbudowany na podstawie klas zdefiniowanych w module
cgi, co pozwala na u¿ywanie kodu napisanego dla protoko³u CGI z poziomu
modu³u mod_python.

%package fcgi
Summary:	A connector to use the abstraction layer with the FastCGI protocol
Summary(pl):	£±cznik pomiêdzy warstwy abstrakcyjn± a protoko³em FastCGI
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description fcgi
The jon-fcgi module builds upon the classes defined in the cgi module
to provide an implementation of the FastCGI protocol. Code originally
written with the CGI protocol in mind can be used unchanged with the
FastCGI protocol by using this module. The module implements the
entire FastCGI specification version 1.0, including multiple
simultaneous connections per process and multiple simultaneous
requests per connection. Requests are executed using Python's
threading facilities, although it can be configured to run without
using threading.

%description fcgi -l pl
Modu³ jon-fcgi jest zbudowany na podstawie klas zdefiniowanych w module
cgi, daj±c implementacjê protoko³u FastCGI. Kod oryginalnie napisany z
my¶l± o protokole CGI mo¿e byæ u¿ywany bez zmian przy u¿yciu tego modu³u
razem z protoko³em FastCGI. Ten modu³ jest implementacj± pe³nej
specyfikacji FastCGI w wersji 1.0, w³±cznie z wieloma jednoczesnymi
po³±czeniami dla procesu oraz wieloma jednoczesnymi ¿±daniami dla
po³±czenia. ¯±dania s± wykonywane przy wsparciu pythonowych w±tków.  ale
mo¿na modu³ skonfigurowaæ tak, by w±tków nie u¿ywa³.

%package mime
Summary:	A simple MIME parser for reading multipart/form-data HTTP requests
Summary(pl):	Prosty parser MIME do czytania ¿±dañ HTTP multipart/form-data
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description mime
The jon-mime module provides a simple MIME-parsing class. It is only
included because the standard Python mimetools/multifile libraries are
too buggy to use for parsing multipart/form-data HTTP requests.

%description mime -l pl
Modu³ jon-mime zawiera prost± klasê analizuj±c± MIME. Jest do³±czona
tutaj tylko dlatego, ¿e standardowe biblioteki Pythona mimetools i
multifile maj± zbyt du¿o b³êdów, by u¿ywaæ ich do analizy ¿±dañ HTTP
multipart/form-data.

%package wt
Summary:	A simple yet extremely powerful web templating system
Summary(pl):	Prosty, o du¿ych mo¿liwo¶ciach system szablonów dla WWW
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description wt
The jon-wt module provides an object-oriented HTML templating system.
The design goals of the system were that it should be very simple,
that it should involve very low overhead in terms of code repeated per
page, that it should achieve as completely as possible the separation
of code and data, and that it should promote modular code re-use.

%description wt -l pl
Modu³ jon-wt daje zorientowany obiektowo system szablonów HTML. Celami tego
systemu by³y: prostota, mo¿liwie najmniejszy narzut w postaci kodu
powtarzanego na stronie, jak najwiêksze odseparowanie kodu od danych oraz
wielokrotne u¿ywanie modularnego kodu.

%package session
Summary:	Session management for HTTP requests
Summary(pl):	Zarz±dzenie sesj± dla ¿±dañ HTTP
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description session
The session jon-module provides way to group HTTP requests into
"sessions" so that information can be maintained between an individual
user's requests to various parts of a web site - for example, so that
a user can "log in" to the web site and their username remembered as
they navigate the site.

%description session -l pl
Modu³ jon-session daje sposób na grupowanie ¿±dañ HTTP w "sesje" tak,
¿e informacje mog± byæ przechowywane pomiêdzy poszczególnymi ¿±daniami
u¿ytkownika w stosunku do ró¿nych czê¶ci serwisu, np.:
u¿ytkownik mo¿e siê zalogowaæ, a jego nazwa jest pamiêtana w czasie
gdy przemieszcza siê po stronie.

# not present in sources (yet?)
#%package dbpool
#Summary: A database connection pool
#Group: Development/Languages/Python
#%pyrequires_eq python
#Requires: %{name} = %{version}

#%description dbpool
#The dbpool module is a wrapper for Python DB-API 2.0-compliant
#database modules to (a) keep a pool of physical connections available
#and (b) upgrade the modules to threadsafety level 2, which means that
#threads can share logical database connections.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENCE README doc/*
%dir %{py_sitedir}/jon
%{py_sitedir}/jon/__init__.py?
%{py_sitedir}/jon/fakefile.py?

%files cgi
%defattr(644,root,root,755)
%{py_sitedir}/jon/cgi.py?

%files fcgi
%defattr(644,root,root,755)
%{py_sitedir}/jon/fcgi.py?

%files mime
%defattr(644,root,root,755)
%{py_sitedir}/jon/mime.py?

%files modpy
%defattr(644,root,root,755)
%{py_sitedir}/jon/modpy.py?

%files session
%defattr(644,root,root,755)
%{py_sitedir}/jon/session.py?

%files wt
%defattr(644,root,root,755)
%dir %{py_sitedir}/jon/wt
%{py_sitedir}/jon/wt/*.py?
