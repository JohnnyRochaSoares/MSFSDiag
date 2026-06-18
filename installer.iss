[Setup]
AppName=MSFSDiag
AppVersion=1.0.0
AppPublisher=João Rocha Soares
DefaultDirName={localappdata}\MSFSDiag
DefaultGroupName=MSFSDiag
PrivilegesRequired=lowest
OutputDir=installer
OutputBaseFilename=MSFSDiag_Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "build\windows\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{userprograms}\MSFSDiag"; Filename: "{app}\MSFSDiag.exe"
Name: "{userdesktop}\MSFSDiag"; Filename: "{app}\MSFSDiag.exe"

[Run]
Filename: "{app}\MSFSDiag.exe"; Description: "Abrir MSFSDiag"; Flags: postinstall skipifsilent
