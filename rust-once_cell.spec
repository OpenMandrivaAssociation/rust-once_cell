%bcond_with check
%global debug_package %{nil}

%global crate once_cell

Name:           rust-%{crate}
Version:        1.19.0
Release:        1
Summary:        Single assignment cells and lazy values

# Upstream license specification: MIT OR Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/once_cell
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
%if %{with check}
BuildRequires:  (crate(crossbeam-utils/default) >= 0.8 with crate(crossbeam-utils/default) < 0.9.0)
BuildRequires:  (crate(lazy_static/default) >= 1.0.0 with crate(lazy_static/default) < 2.0.0)
BuildRequires:  (crate(regex/default) >= 1.2.0 with crate(regex/default) < 2.0.0)
%endif
%endif

%global _description %{expand:
Single assignment cells and lazy values.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(once_cell) = 1.7.2
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(once_cell/default) = 1.7.2
Requires:       cargo
Requires:       crate(once_cell) = 1.7.2
Requires:       crate(once_cell/std) = 1.7.2

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(once_cell/alloc) = 1.7.2
Requires:       cargo
Requires:       crate(once_cell) = 1.7.2
Requires:       crate(once_cell/race) = 1.7.2

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+parking_lot-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(once_cell/parking_lot) = 1.7.2
Requires:       cargo
Requires:       (crate(parking_lot) >= 0.11.0 with crate(parking_lot) < 0.12.0)
Requires:       crate(once_cell) = 1.7.2

%description -n %{name}+parking_lot-devel %{_description}

This package contains library source intended for building other packages
which use "parking_lot" feature of "%{crate}" crate.

%files       -n %{name}+parking_lot-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+race-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(once_cell/race) = 1.7.2
Requires:       cargo
Requires:       crate(once_cell) = 1.7.2

%description -n %{name}+race-devel %{_description}

This package contains library source intended for building other packages
which use "race" feature of "%{crate}" crate.

%files       -n %{name}+race-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(once_cell/std) = 1.7.2
Requires:       cargo
Requires:       crate(once_cell) = 1.7.2
Requires:       crate(once_cell/alloc) = 1.7.2

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(once_cell/unstable) = 1.7.2
Requires:       cargo
Requires:       crate(once_cell) = 1.7.2

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages
which use "unstable" feature of "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
