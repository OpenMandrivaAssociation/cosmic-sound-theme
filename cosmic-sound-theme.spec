%undefine _debugsource_packages
Name:           cosmic-sound-theme
Version:        1.7.0
#define beta beta.7
Release:        %{?beta:0.%{beta}.}1
Summary:        Sound theme for the COSMIC desktop environment
Group:          Desktop/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-sound-theme
Source0:	https://github.com/pop-os/cosmic-sound-theme/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz

BuildRequires:  meson

%description
The source file is the .mmpz file; it's a standard LMMS project, and uses only default instruments and effects. It was created in LMMS 1.2, but it may work in LMMS 1.1.3 as well. Each different sound is its own track, and there's a segment for each sound. Some tracks may require trimming to ensure they don't have too much silence. Be sure to apply a compressor and to normalize the sounds to ensure that chords aren't excessively loud and single-notes aren't too quiet. The ideal peak seems to be close to 0.6-ish in Audacity.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%{_datadir}/sounds/COSMIC/
