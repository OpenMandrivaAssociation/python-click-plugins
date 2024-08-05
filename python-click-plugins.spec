%global srcname click-plugins
%global srcname_no_dash click_plugins

Name:           python-%{srcname}
Version:        1.1.1
Release:        4
Summary:        Click extension to register CLI commands via setuptools
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:	https://files.pythonhosted.org/packages/source/c/click-plugins/click-plugins-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-click >= 4.0
BuildArch:      noarch

%description
An extension module for click to register external CLI commands via setuptools
entry-points.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/%{srcname_no_dash}
%{python_sitelib}/%{srcname_no_dash}-%{version}-py*.egg-info
