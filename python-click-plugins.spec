%global srcname click-plugins
%global srcname_no_dash click_plugins

Name:           python-%{srcname}
Version:        1.1.1
Release:        2
Summary:        Click extension to register CLI commands via setuptools
%global _description \
An extension module for click to register external CLI commands via setuptools \
entry-points.
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:	https://files.pythonhosted.org/packages/5f/1d/45434f64ed749540af821fd7e42b8e4d23ac04b1eda7c26613288d6cd8a8/click-plugins-1.1.1.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-click >= 4.0
BuildArch:      noarch

%description %{_description}


%prep
%autosetup -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/%{srcname_no_dash}
%{python_sitelib}/%{srcname_no_dash}-%{version}-py?.?.egg-info
