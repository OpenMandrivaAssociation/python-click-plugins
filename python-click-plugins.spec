%global module click-plugins
%global oname click_plugins

Name:		python-click-plugins
Version:	1.1.1.2
Release:	1
Summary:	Click extension to register CLI commands via setuptools
Group:		Development/Python
License:	MIT
URL:		https://pypi.python.org/pypi/click-plugins
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(click) >= 4.0
BuildArch:	noarch

%description
An extension module for click to register external CLI commands via setuptools
entry-points.

%prep
%autosetup -p1 -n %{oname}-%{version}
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}*.*-info
