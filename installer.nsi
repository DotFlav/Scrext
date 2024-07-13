; NSIS Skript für All-in-One-Installer

OutFile "ScrextInstaller.exe"
InstallDir $PROGRAMFILES\Scrext

; MUI 1.67 kompatibel -----
!include "MUI.nsh"

!define MUI_ABORTWARNING

!insertmacro MUI_PAGE_WELCOME
;!insertmacro MUI_PAGE_LICENSE "license.txt"  ; Diese Zeile entfernen, wenn keine Lizenzseite benötigt wird
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

; MUI Einstellungen
; ------------------

Name "Scrext"
Caption "Scrext Installer"
Icon "images\kitty.ico"

Section "MainSection" SEC01
    SetOutPath $INSTDIR

    ; Hauptanwendung kopieren
    File "dist\app.exe"

    ; Icon und andere Bilder kopieren
    SetOutPath $INSTDIR\images
    File "images\kitty.ico"

    ; OCR-Unterordner erstellen und Dateien kopieren
    SetOutPath $INSTDIR\OCR
    File /r "Tesseract-OCR\*.*"

    ; Installationsdateien kopieren
    SetOutPath $INSTDIR\installations
    File "installations\python-3.12.3.exe"  ; Ersetzen Sie durch den tatsächlichen Dateinamen
    File "installations\requirements.txt"

    ; Python installieren (falls nicht vorhanden)
    IfFileExists "$PROGRAMFILES\Python\python.exe" python_installed python_not_installed
    python_installed:
        MessageBox MB_OK "Python ist bereits installiert."
        Goto done_python_install
    python_not_installed:
        ExecWait '"$INSTDIR\installations\python-3.12.3.exe" /quiet InstallAllUsers=1 PrependPath=1'  ; Ersetzen Sie durch den tatsächlichen Dateinamen
    done_python_install:

    ; Pip-Anforderungen installieren
    ExecWait '"$PROGRAMFILES\Python\python.exe" -m pip install -r "$INSTDIR\installations\requirements.txt"'

    ; Uninstaller schreiben
    WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

Section -AdditionalIcons
    CreateShortCut "$DESKTOP\Scrext.lnk" "$INSTDIR\app.exe"
SectionEnd

; Uninstall
Section "Uninstall"
    Delete "$DESKTOP\Scrext.lnk"
    Delete "$INSTDIR\app.exe"
    Delete "$INSTDIR\installations\requirements.txt"
    Delete "$INSTDIR\installations\python-3.12.3.exe"  ; Ersetzen Sie durch den tatsächlichen Dateinamen
    Delete "$INSTDIR\images\kitty.ico"
    RMDir /r "$INSTDIR\OCR"
    RMDir "$INSTDIR\installations"
    RMDir "$INSTDIR\images"
    ; Uninstaller löschen, nachdem alles andere entfernt wurde
    Delete "$INSTDIR\Uninstall.exe"
    RMDir "$INSTDIR"
SectionEnd
