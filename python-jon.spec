%include	/usr/lib/rpm/macros.python

Summary:	Jon's Python modules (jonpy)
Name:		python-jon
Version:	0.03
Release:	0.1
License:	Custom
Group:		Libraries/Python
Source0:	http://prdownloads.sourceforge.net/jonpy/jonpy-%{version}.tar.gz
URL:		http://jonpy.sourceforge.net/
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These Python modules provide simple yet powerful multi-threaded
object-oriented CGI/FastCGI/mod_python/html-templating facilities for
the Python programming language.

%package cgi
Summary:	Abstraction layer for CGI-style applications
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description cgi
The jon-cgi module provides an object-oriented interface for writing
CGI and CGI-style programs. It provides an abstraction layer so that
the same code can be used with either standard CGI or replacement
technologies such as FastCGI.

%package modpy
Summary:	A connector to use the abstraction layer with mod_python
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description modpy
The jon-modpy module builds upon the classes defined in the cgi module
to allow code originally written with the CGI protocol in mind to be
used unchanged with the mod_python module.

%package fcgi
Summary:	A connector to use the abstraction layer with the FastCGI protocol
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

%package mime
Summary:	A simple MIME parser for reading multipart/form-data HTTP requests
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description mime
The jon-mime module provides a simple MIME-parsing class. It is only
included because the standard Python mimetools/multifile libraries are
too buggy to use for parsing multipart/form-data HTTP requests.

%package wt
Summary:	A simple yet extremely powerful web templating system
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description wt
The jon-wt module provides an object-oriented HTML templating system.
The design goals of the system were that it should be very simple,
that it should involve very low overhead in terms of code repeated per
page, that it should achieve as completely as possible the separation
of code and data, and that it should promote modular code re-use.

%package session
Summary:	Session management for HTTP requests
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description session
The session jon-module provides way to group HTTP requests into
"sessions" so that information can be maintained between an individual
user's requests to various parts of a web site - for example, so that
a user can "log in" to the web site and their username remembered as
they navigate the site.

# not present in sources (yet?) #%package dbpool #Summary: A database
connection pool #Group: Development/Languages/Python #%pyrequires_eq
python #Requires: %{name} = %{version} # #%description dbpool #The
dbpool module is a wrapper for Python DB-API 2.0-compliant database
modules #to (a) keep a pool of physical connections available and (b)
upgrade the #modules to threadsafety level 2, which means that threads
can share logical #database connections.

%prep
%setup -q -n jonpy-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT

cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

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
