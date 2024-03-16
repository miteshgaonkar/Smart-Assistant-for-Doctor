; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "SMART ASSISTANT FOR DOCTORS"
#define MyAppVersion "1.0"
#define MyAppPublisher "TIMBA, Inc."
#define MyAppURL "http://aihealthcare.000webhostapp.com"
#define MyAppExeName "sa.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{0F3707E4-C058-4153-A733-5743B11EABF6}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DisableProgramGroupPage=yes
OutputDir=C:\Users\acer\Desktop\SMART ASSISTANT FOR DOCTORS SETUP
OutputBaseFilename=smart-assistant-for-doctors-setup
SetupIconFile=E:\Adventure Sports\10-512.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "F:\final year project\project\sa.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\dataset_uncleaned.csv"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\intro.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\intro2.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\logo.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\logo_complete.JPG"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\pcvoice.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\pcvoice1.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\pcvoice3.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\pop_reg.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\pop_reg1.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\pop1.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\popup.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\readme.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\sa.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\sa.spec"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\Testing.csv"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\Training.csv"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\final year project\project\uncleand.csv"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

